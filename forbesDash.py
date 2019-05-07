import pandas as pd
import statistics as stats
import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# import data
forbes1 = pd.read_csv("forbes1.csv", header = None)
forbes2 = pd.read_csv("forbes2.csv", header = None) 

# tidy forbes2
forbes2.drop_duplicates
forbes2.columns = ['CompRank', 'Market Capitalization', 'Industry', 'Founded', 'Country', 'Chairman', 'Employees']
forbes2[["Rank", "Name"]] = forbes2['CompRank'].str.split(n = 1, expand = True)
forbes2 = forbes2.drop(['CompRank'], axis = 1)
forbes2.columns = ['Market Value', 'Industry', 'Founded', 'Country', 'Chairman', 'Employees', 'Rank', 'Company']

# rename forbes1 columns
forbes1.columns = ['Company', 'Country', 'Sales', 'Profits', 'Assets', 'Market Value']

# merge the dataframes and tidy
forbes = forbes2.merge(forbes1, on = 'Company')
forbes = forbes.drop("Market Value_x", axis = 1)
forbes = forbes.drop("Country_x", axis = 1)
cols = forbes.columns.tolist()
cols = ['Rank', 'Company', 'Country_y', 'Industry', 'Assets', 'Sales', 'Profits', 'Market Value_y', 'Employees', 'Founded', 'Chairman']
forbes = forbes[cols]
forbes = forbes.rename(columns = {'Country_y': 'Country', 'Market Value_y': 'Market Capitalization'})

# Countries histogram data
forbes_CountryCount = forbes.groupby('Country').count()
cols = forbes_CountryCount.columns.tolist()
cols = ['Rank']
forbes_CountryCount = forbes_CountryCount[cols]
forbes_CountryCount = forbes_CountryCount.rename(columns = {'Rank': 'Count'})
forbes_CountryCount = forbes_CountryCount.sort_values(by = ['Count'], ascending = False)
forbes_CountryCount = forbes_CountryCount.iloc[:27]






app = dash.Dash()

app.layout = html.Div(children = [
    html.H1('Web Scraping Project'),
    dcc.Graph(id = 'Country_histogram',
        figure = {
            data = [x = 'forbes_CountryCount["Country"]', y = 'forbes_CountryCount["Count"]', 'type' = 'bar', 'name' = 'First']
        })
    ]) 

if __name__ == '__main__':
    app.run_server(debug = False)
