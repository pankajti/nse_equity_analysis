from nse_equity_analysis.database.connection.db_connection import *
from nse_equity_analysis.database.schema.db_model import AccessTockens



def get_tocken(provider , type):
    api_key = get_session().query(AccessTockens).filter(AccessTockens.provider == provider,
                                                        AccessTockens.tocken_type == type).all()[0].tocken
    return api_key

quandl_api_key= get_tocken('quandl','api_key')
quandl_codes_url='https://www.quandl.com/api/v3/databases/NSE/codes?api_key={}'.format(quandl_api_key)

