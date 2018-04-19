from selenium import webdriver
from bs4 import BeautifulSoup

def get_portfolio_info(scheme_code):
    browser =webdriver.PhantomJS()
    browser.get('http://www.moneycontrol.com/mutual-funds/idfc-focused-equity-fund-regular-plan/portfolio-holdings/MAG096')
    source=browser.page_source
    soup=BeautifulSoup(source)
    table=soup.find_all(class_='tblporhd')

    print(source)

get_portfolio_info(5006)