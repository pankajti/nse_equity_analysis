import pandas as pd
from nse_equity_analysis.database.connection import db_connection

sql_format='select * from nse_historic_data where equity_id={}'

yesbank_data=pd.read_sql(sql=sql_format.format(1430),con=db_connection.get_connection())
nifty_data=pd.read_sql(sql=sql_format.format(1652),con=db_connection.get_connection())

print('aa')