import matplotlib
import matplotlib.pyplot as plt
from sqlalchemy.sql import text
from nse_equity_analysis.database.schema.db_model import EquityCode, NseHistoricData
import pandas as pd

from nse_equity_analysis.database.connection import db_connection
session =db_connection.get_session()


def update_split_ratio():
    stmt = text('select * from stock_split_detail')
    result = db_connection.get_connection().execute(stmt)
    data = pd.DataFrame(result.fetchall())
    data['split_ratio'] = data[4] / data[5]
    data['split_ratio'] = data['split_ratio'].apply(lambda s: s if s < 1 else 1 / s)
    for idx, row in data.iterrows():
        hist_rec = session.query(NseHistoricData).filter(NseHistoricData.equity_id == row[0],
                                                         NseHistoricData.trade_date < row[3]). \
            update({NseHistoricData.split_ratio: NseHistoricData.split_ratio * row['split_ratio']})
        print('{} rows updated for {}'.format(hist_rec, row[1]))
    session.commit()

update_split_ratio()






