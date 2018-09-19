import quandl
import requests
import pandas as pd
from io import StringIO,BytesIO
from zipfile import ZipFile
from  nse_equity_analysis.database.connection import db_connection
from nse_equity_analysis.database.dao import GenericDao
from nse_equity_analysis.database.schema.db_model import EquityCode, NseHistoricData
from nse_equity_analysis.config import api_config
import time
from sqlalchemy.sql import text


stmt = text('select id , code from equity_code  ec where ec.id not in (select distinct equity_id from nse_historic_data)')
result = db_connection.get_connection().execute(stmt)
pd_data = pd.DataFrame(result.fetchall())

for idx, record in pd_data.iterrows():
    print('loading data for {}'.format(record))
    time.sleep(20)
    try:
        #str_records = record.decode('utf-8').split(',')
        #equity_code = EquityCode()
        #equity_code.code = str_records[0]
        #equity_code.name = str_records[1]

        data = quandl.get(record[1])
        #GenericDao.insert_record(equity_code)
        #equity_id = equity_code.id
        for data_idx, data_rec in data.iterrows():
            hist_data = NseHistoricData()
            hist_data.close = data_rec['Close']
            if 'Last' in data:
                hist_data.open = data_rec['Open']
                hist_data.last = data_rec['Last']
                hist_data.high = data_rec['High']
                hist_data.low = data_rec['Low']
                hist_data.total_trade_qty = data_rec['Total Trade Quantity']
                hist_data.turnover = data_rec['Turnover (Lacs)']
                hist_data.split_ratio=1
            hist_data.equity_id = record[0]
            hist_data.trade_date = data_idx.date()
            GenericDao.insert_record(hist_data)
    except Exception as e:
        print('error ' + str(e))

#print(data)