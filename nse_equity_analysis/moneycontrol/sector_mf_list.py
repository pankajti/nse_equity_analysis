
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter


def get_portfolio_info(scheme_name,scheme_code):
    print('processing {}'.format(scheme_name))
    browser =webdriver.Firefox()
    browser.get('http://www.moneycontrol.com/mutual-funds/{}/portfolio-holdings/{}'.format(scheme_name,scheme_code))
    source=browser.page_source
    soup=BeautifulSoup(source,'lxml')
    table=soup.find_all(class_='tblporhd')
    try :
        rows = table[0].find_all('tr')
        stock_df= pd.DataFrame()
        print('{} rows for scheme {}  code {} '.format(len(rows),scheme_name, scheme_code))
        for row in rows:
            columns=row.find_all('td')
            if len(columns)<5  or len(columns)>12 :
                continue
            stock_df=stock_df.append({'MF_NAME':scheme_name,'MF_CODE':scheme_code, 'Equity':columns[0].text,'Sector':columns[1].text,'Qty':columns[2].text,'Value':columns[3].text,'Percentage':columns[4].text},ignore_index=True )
    except Exception as e :
        print('exception during {} '.format(scheme_name))

        print(str(e))

    browser.close()
    return stock_df

def get_mf_list(sector):
    url = 'http://www.moneycontrol.com/mutual-funds/performance-tracker/returns/{}.html'.format(sector)
    browser =webdriver.Firefox()
    browser.get(url)
    source=browser.page_source
    soup=BeautifulSoup(source,'lxml')
    table=soup.find_all(class_='gry_t')
    try :
        rows = table[0].find_all('tr')
        cleaned_href={}
        for row in rows:
            columns=row.find_all('td')
            if len(columns)<5  or len(columns)>12 or columns[0].a==None:
                continue
            href=columns[0].a.attrs['href']
            href_comps= href.split('/')
            cleaned_href_name=href_comps[-2].replace('-dp-g', '-rp-g')
            cleaned_href_name=cleaned_href_name.replace('-fund-rp', '-fund-dp')
            cleaned_href_name=cleaned_href_name.replace('-direct', '')
            cleaned_href_name=cleaned_href_name.replace('-direct', '')

            cleaned_href[cleaned_href_name]=href_comps[-1]
        print('total {} mfs in {} sector '.format(len(cleaned_href),sector))
        for key in cleaned_href:
            stocks_frame = get_portfolio_info(key, cleaned_href[key])
            stocks_frame.to_csv('data/{}stocks.csv'.format(sector),mode='a',index=False,header=False)
    except Exception as e :
        print('exception during sector  {} '.format(sector))

        print(str(e))
    browser.close()


get_mf_list('small-and-mid-cap')