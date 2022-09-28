import os
import pandas as pd
import datetime as dt
import json
from nse_equity_analysis.database.dao.ref.equity_dao import *
DATE_FMT = lambda x: '{}-{}-{}'.format(x[0:4], x[4:6], x[6:8])
from nse_equity_analysis.database.schema.equity_db_model import *
from psycopg2.extras import DateRange
import requests


def read_price_data(date):
    t_date = dt.datetime.strptime(date, '%Y%m%d')
    t_date_file_format = t_date.strftime("%b%Y").upper()
    f = f"fo{date[6:]}{t_date_file_format}bhav.csv.zip"
    try:

        url = f'https://www1.nseindia.com/content/historical/DERIVATIVES/{f[7:11]}/{f[4:7]}/{f}'
        headers = {'User-Agent': 'mybot', 'Accept': '*/*',
                   "Referer": "https://www.nseindia.com/products/content/equities/equities/archieve_eq.htm"}
        r = requests.get(url, headers=headers)
        #data = BytesIO(r.content)
        if r.status_code == 200:
            file_path= f'{f}'
            with open(file_path, 'wb') as r_file:
                r_file.write(r.content)
                print(f"file {f} downloaded")
        else:
            print(f"file {f} could not be read code  {r.status_code}  reason {r.reason}")

        # print(f"done for {f}")
    except Exception as e:
        print(f"file {f} could not be read")
        raise e


if __name__ == '__main__':
    start_date = dt.date(2014,11,20)
    end_date = dt.datetime.now().date()
    dates = pd.bdate_range(start_date, end_date)
    for d in dates:
        load_date = d.strftime('%Y%m%d')
        price_data = read_price_data(load_date)

