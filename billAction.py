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

flBillInfo = 'flBillInfo.csv'

def getInfo(flBillInfo, soup):
    info = open(flBillInfo, 'w')
    c = csv.writer(info)
    c.writerow( ['Bill Number', 'Title', 'Filled By', 'Last Action'])
    bills = soup.find('tbody')
    buttons = soup.find('a', class_='next')
    for bill in bills.find_all('tr'):
        info.write(bill.text.strip() + '\n')
        for n in range(2):
                driver.find_element_by_css_selector('.next').click()
                s = randint(1, 10)
                time.sleep(s)
                for bill in bills.find_all('tr'):
                    info.write(bill.text.strip() + '\n')

    info.close()

getInfo(flBillInfo, soup)
