from nse_equity_analysis.database.connection import db_connection

def insert_record(record):
    session =db_connection.get_session()
    session.add( record)
    session.commit()
    session.flush()


 


