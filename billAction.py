import time
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup
import requests
import csv

driver = webdriver.Chrome('C:\\Users\\alexl\\OneDrive\\Documents\\Web Apps\\python\\scraping\\scrapingProject\\chromedriver')
driver.get('https://www.flsenate.gov/Session/Bills/2022')

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

table = soup.find('tbody')
bills = table.find_all('tr')

def billItems(bill):
    items = bill.find_all('td')
    number = bill.find('th')
    billList = []
    billList.append(number.text)
    for item in items[0:3]:
        billList.append(item.text.strip())
    href = number.find('a').attrs['href']
    billList.append(href)
    return billList

flBillInfo = 'flBillInfo.csv'
info = open(flBillInfo, 'w')
c = csv.writer(info)
c.writerow( ['Bill Number', 'Title', 'Filled By', 'Last Action'])

for bill in bills:
    c.writerow( billItems(bill) )

info.close()

while True:
    try:
        nextPage = driver.find_element_by_css_selector('.next').get_attribute('href')
        driver.find_element_by_css_selector('.next').click()
        s = randint(1, 5)
        time.sleep(s)
        driver.get(str(nextPage))
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        for bill in bills:
            info = open(flBillInfo, 'a')
            c.writerow( billItems(bill) )

    except:
        break
        info.close()
