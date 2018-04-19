from selenium import webdriver
from bs4 import BeautifulSoup

def get_portfolio_info(scheme_name,scheme_code):
    browser =webdriver.PhantomJS()
    browser.get('http://www.moneycontrol.com/mutual-funds/{}/portfolio-holdings/{}'.format(scheme_name,scheme_code))
    source=browser.page_source
    soup=BeautifulSoup(source)
    table=soup.find_all(class_='tblporhd')
    rows = table[0].find_all('tr')
    for row in rows:
        columns=row.find_all('td')
        format_str='{},'*len(columns)

        all_cols=[column.text for column in columns]
        print(format_str.format(*all_cols))

    #print(source)
get_portfolio_info('idfc-focused-equity-fund-regular-plan','MAG096')