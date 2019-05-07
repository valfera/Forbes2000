from selenium import webdriver
import csv


driver = webdriver.Chrome(r'C:\Users\valfe\Desktop\chromedriver.exe')
driver.get('https://www.forbes.com/companies/icbc/?list=global2000#6a46fd731679')


page_info = {}


# Create csv file
csv_file = open("Forbes3.csv", 'w', encoding = 'utf-8', newline = '')
writer = csv.writer(csv_file)


for i in range(2000):

    company = driver.find_element_by_xpath('//div[@class="profile-heading--desktop"]/h1').text
    market_cap = driver.find_element_by_xpath('//span[@class="profile-row--value profile-row--valuation-value"]').text
    items_list = driver.find_elements_by_xpath('//span[@class="profile-row--value"]')
    industry = items_list[0].text
    founded = items_list[1].text
    chairman = items_list[2].text
    employees = items_list[3].text
    headquarters = items_list[4].text
        
    print(company)

    # create dictionary
    page_info['company'] = company
    page_info['market_cap'] = market_cap
    page_info['industry'] = industry
    page_info['founded'] = founded
    page_info['chairman'] = chairman
    page_info['employees'] = employees
    page_info['headquarters'] = headquarters


    writer.writerow(page_info.values())


    button = driver.find_element_by_xpath('//a[@class="profile-nav__next"]')
    button.click()


csv_file.close()
driver.close()
