import quandl
import requests
import pandas as pd
from io import StringIO,BytesIO
from zipfile import ZipFile

from nse_equity_analysis.database.dao import GenericDao
from nse_equity_analysis.database.schema.db_model import EquityCode, NseHistoricData
from nse_equity_analysis.config import config
import time
import datetime as dt
def load_historic_data():
    api_key = config.quandl_api_key
    st_Time = time.time()
    quandl.ApiConfig.api_key = api_key
    codes_url = config.quandl_codes_url
    codes_data = requests.get(codes_url)
    zipped_file = ZipFile(BytesIO(codes_data.content))
    file = zipped_file.open('NSE-datasets-codes.csv')
    records = file.readlines()


    for record in records:
        try:
            str_records = record.decode('utf-8').split(',')
            equity_code=EquityCode()
            equity_code.code=str_records[0]
            equity_code.name=str_records[1]
            GenericDao.insert_record(equity_code)
            equity_id=equity_code.id
            data=quandl.get(str_records[0])
            for data_idx,data_rec in data.iterrows():
                hist_data=NseHistoricData ()
                hist_data.close=data_rec['Close']
                if 'Last' in data:
                    hist_data.open=data_rec['Open']
                    hist_data.last=data_rec['Last']
                    hist_data.high=data_rec['High']
                    hist_data.low=data_rec['Low']
                    hist_data.total_trade_qty=data_rec['Total Trade Quantity']
                    hist_data.turnover=data_rec['Turnover (Lacs)']
                hist_data.equity_id = equity_id
                hist_data.trade_date=data_idx.date()
                GenericDao.insert_record(hist_data)
        except Exception as e:
            print('error '+str(e))


