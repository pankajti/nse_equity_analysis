
from nse_equity_analysis.database.schema.db_model import EquityCode,NseHistoricData
from nse_equity_analysis.database.connection import db_connection
import pandas as pd

query='select * from nse_historic_data where equity_id ={} order by trade_date'

records=pd.read_sql(query.format(1430),db_connection.get_connection())
records.set_index('trade_date', inplace=True)
base_close_data=records.loc[:,['close']]

with open('/Users/pankaj/dev/git/nse_equity_analysis/nse_equity_analysis/analysis/data/yesbank_corr_data.csv','a') as result_file:
    for i in range(2200):
        records2=pd.read_sql(query.format(i), db_connection.get_connection())
        if len(records2)!=0:
            records2.set_index('trade_date',inplace=True)
            corr=base_close_data.corrwith(records2['close'])
            code=db_connection.get_session().query(EquityCode).filter_by(id=i).first()
            result_file.write('{},{}\n'.format(code.name.strip(),corr[0]))
            result_file.flush()