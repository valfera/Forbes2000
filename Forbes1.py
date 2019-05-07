from selenium import webdriver
import time
import csv

driver = webdriver.Chrome(r'C:\Users\valfe\Desktop\chromedriver.exe')
driver.get('https://www.forbes.com/global2000/list/#tab:overall')


SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(new_height)
    if new_height == last_height:
        break
    last_height = new_height


driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
rows = driver.find_elements_by_xpath('//tr[@class="data"]')


info = {}

print('write to csv')

# Create csv file
csv_file = open("Forbes1.csv", 'w', encoding = 'utf-8', newline = '')
writer = csv.writer(csv_file)

print(len(rows))

for row in rows:

    company = row.find_element_by_xpath('./td[@class="name"]/a').text
    country = row.find_element_by_xpath('.//td[4]').text
    sales = row.find_element_by_xpath('.//td[5]').text
    profits = row.find_element_by_xpath('.//td[6]').text
    assets = row.find_element_by_xpath('.//td[7]').text
    market_value = row.find_element_by_xpath('.//td[8]').text

    print(company)


    info['company'] = company
    info['country'] = country
    info['sales'] = sales
    info['profits'] = profits
    info['assets'] = assets
    info['market_value'] = market_value


    writer.writerow(info.values())

    

csv_file.close()

driver.close()




