from nse_equity_analysis.database.schema.db_model import AccessTockens
from nse_equity_analysis.database.dao import GenericDao
from nse_equity_analysis.database.schema.db_model import create_schema


def add_tocken(provider, tocken_text , tocken_type):
    tocken = AccessTockens()
    tocken.provider = provider
    tocken.tocken = tocken_text
    tocken.tocken_type = tocken_type
    GenericDao.insert_record(tocken)

create_schema()


add_tocken('aaa','aaa','aaa')


