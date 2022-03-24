import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from collections import defaultdict

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime as dt
import schedule

def main():
    browser = webdriver.Firefox()
    browser.get("https://www.99.co/singapore/rent")

    homes = defaultdict(list)
    t = dt.datetime.now()


    next_button = browser.find_elements_by_class_name('next')
    time.sleep(3)

    while len(next_button) >0:
        soup = BeautifulSoup(browser.page_source)
        if len(soup.find_all(class_='next disabled'))>0:
            break
        links = soup.find_all('a', rel='noopener noreferrer')
        data = soup.find_all(attrs={'data-cy': 'listingCard'})
        print("scraping {}".format(soup.h1.text))

        for idx, d in enumerate(data[::2]) :
            recs = d.find_all('p')
            records = [rec.text for rec in recs]
            records.append(links[idx].text)
            link =links[idx]['href']
            l = link[:link.index('#') if '#' in link else -1]
            records.insert(0,l)
            records.append(str(len(records)))
            records.append(str(t.strftime('%Y%d%m %H%M%S')))
            homes[len(records)].append(records)
            str_rec = '~'.join(records)

            with open('records.csv', 'a') as f:
                f.write(str_rec+"\n")
        next_button[0].click()
        time.sleep(4)
        next_button = browser.find_elements_by_class_name('next')



if __name__ == '__main__':
    main()
    schedule.every(3).hours.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)


