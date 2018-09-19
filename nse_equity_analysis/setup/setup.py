from nse_equity_analysis.database.schema import db_model
from nse_equity_analysis.quandl import historic_data
from nse_equity_analysis.motilal import stock_split
from nse_equity_analysis.database.dao import historic_data_dao

# create Schema
db_model.create_schema()

# download quandl data
#historic_data.load_historic_data()

#download split data from motilal

#stock_split.populate_db_from_page_data()

# stock update split data

historic_data_dao.update_split_ratio()

# find correlation