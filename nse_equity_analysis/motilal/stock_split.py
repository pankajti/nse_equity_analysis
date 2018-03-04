from selenium import webdriver

from bs4 import BeautifulSoup
from nse_equity_analysis.database.schema.db_model import EquitySplit
from nse_equity_analysis.database.dao import GenericDao
from nse_equity_analysis.config import config
import time
def populate_db_from_page_data():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for row in soup.find_all('tr'):
        columns=row.find_all('td')
        equity_split = EquitySplit()
        if len(columns)!=0:
            equity_split.company_name =columns[0].text
            equity_split.record_date =columns[1].text
            equity_split.split_date =columns[2].text
            equity_split.face_value_after =float(columns[3].text)
            equity_split.face_value_before =float(columns[4].text)
            GenericDao.insert_record(equity_split)
    disabled_next = browser.find_elements_by_class_name('paginate_button.next.disabled')
    if  (disabled_next == None or len(disabled_next) == 0):
        browser.find_elements_by_class_name('paginate_button.next')[0].click()
        populate_db_from_page_data()
    else:
        return

browser=webdriver.Firefox()
response=browser.get(config.motilal_split_url)
time.sleep(100)
populate_db_from_page_data()

