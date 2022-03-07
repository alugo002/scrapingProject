import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv

driver = webdriver.Chrome('C:\\Users\\alexl\\OneDrive\\Documents\\Web Apps\\python\\scraping\\scrapingProject\\chromedriver')
driver.get('https://m.flsenate.gov/Senators/List')

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

flSenatorInfo = 'flSenatorInfo.csv'

def get_info(flSenatorInfo, soup):
    info = open(flSenatorInfo, 'w')
    c = csv.writer(info)
    c.writerow( ['Last Name', 'First Name', 'District', 'Party'])
    senators = soup.find('tbody')
    for sen in senators.find_all('tr'):
        sens = str(sen.text.strip())
        if 'Vacant' not in sens:
            print(sens.replace('\n', ',') + '\n')
            info.write(sens.replace('\n', ',') + '\n')
    info.close()

get_info(flSenatorInfo, soup)
