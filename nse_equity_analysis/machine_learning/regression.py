from nse_equity_analysis.database.schema.db_model import NseHistoricData,EquityCode
from sklearn.linear_model import LinearRegression
from nse_equity_analysis.database.connection.db_connection import get_session
import pandas as pd
from  sklearn import metrics
import math
result1=get_session().query(NseHistoricData.open*NseHistoricData.split_ratio,).filter(NseHistoricData.equity_id==1423 ).\
    filter( NseHistoricData.trade_date>'2005-07-12')
result2=get_session().query(NseHistoricData.open*NseHistoricData.split_ratio).\
    filter(NseHistoricData.equity_id==586).filter( NseHistoricData.trade_date>'2005-07-12')

df1=pd.DataFrame(result1.all()[:2000],columns=['open'])

df2=pd.DataFrame(result2.all()[:2000],columns=['open'])

model=LinearRegression()
model.fit(df1,df2)
y_pred=model.predict(result1[2001:2100])
y_real=result2[2001:2100]

print(math.sqrt(metrics.mean_squared_error(y_pred,y_real)))