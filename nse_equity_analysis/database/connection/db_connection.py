
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from nse_equity_analysis.config import config

engine= create_engine(config.db_url)

connection = engine.connect()

def get_connection():
    return connection

def get_dbengine():
    return engine

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()
