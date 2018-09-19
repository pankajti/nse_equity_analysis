from selenium import webdriver
from bs4 import BeautifulSoup
import time

def populate():
    soup=BeautifulSoup(browser.page_source)


week_quote='http://www.dce.com.cn/publicweb/quotesdata/weekQuotesEn.html'

day_q='/publicweb/quotesdata/dayQuotesEn.html'

browser=webdriver.Firefox()
#browser.get('http://www.dce.com.cn/DCE/Market_Data/Market%20Statistics/index.html')
browser.get(week_quote)
browser.find_element_by_xpath('/html/body/form[1]/div/div[1]/div[3]/div/ul[2]/li[2]').click()

soup = BeautifulSoup(browser.page_source)

time.sleep(30)


browser.find_elements_by_xpath('/html/body/form[1]/div/div[1]/div[1]/div/table/tbody/tr[7]/td[5]')[0].click()



print('a')


