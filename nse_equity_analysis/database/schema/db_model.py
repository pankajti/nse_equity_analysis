from sqlalchemy import Column,String,Integer,Numeric,Date,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from nse_equity_analysis.database.connection import db_connection


Base=declarative_base()


class NseHistoricData(Base):
    __tablename__='nse_historic_data'
    id=Column(Integer, primary_key = True)
    trade_date=Column(Date)
    equity_id=Column(Integer, ForeignKey('equity_code.id',ondelete='CASCADE'))
    equity=relationship('EquityCode',backref='equity_codes')
    open=Column(Numeric)
    close=Column(Numeric)
    high=Column(Numeric)
    low=Column(Numeric)
    last=Column(Numeric)
    total_trade_qty=Column(Numeric)
    turnover=Column(Numeric)
    split_ratio=Column(Numeric)



class EquityCode(Base):
    __tablename__='equity_code'
    id=Column(Integer, primary_key = True)
    code=Column(String)
    name=Column(String)


class EquitySplit(Base):
    __tablename__='equity_split'
    id=Column(Integer, primary_key = True)
    company_name=Column(String)
    record_date=Column(String)
    split_date=Column(String)
    face_value_before=Column(Numeric)
    face_value_after=Column(Numeric)

class AccessTockens(Base):
    __tablename__='access_tockens'
    id=Column(Integer,primary_key=True)
    provider=Column(String)
    tocken_type=Column(String)
    tocken=Column(String)



def create_schema():

    Base.metadata.create_all(db_connection.get_dbengine())
    print('schema created ...')



