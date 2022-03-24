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

flBillInfo = 'flBillInfoOld.csv'
info = open(flBillInfo, 'w')
c = csv.writer(info)
c.writerow( ['Bill Number', 'Title', 'Filled By', 'Last Action'])
bills = soup.find('tbody')

for bill in bills.find_all('tr'):
    info.write(bill.text.strip() + '\n')

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
        bills = soup.find('tbody')
        for bill in bills.find_all('tr'):
            info = open(flBillInfo, 'a')
            info.write(bill.text.strip() + '\n')

    except:
        break
        info.close()
