from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy.exc import OperationalError
from sqlalchemy import text


from dotenv import load_dotenv

load_dotenv()

SQLALCHEMNY_DB_URL = "postgresql://postgres:admin@localhost:5432/postgres"
# "postgresql://postgres:admin@localhost/postgres"

engine = create_engine(SQLALCHEMNY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_table():
    engine = sqlalchemy.create_engine(SQLALCHEMNY_DB_URL)
    conn = engine.connect()

    # Create the Table
    conn.execute('COMMIT')
    conn.execute('CREATE TABLE Events')
    conn.close()

def get_db():
    db = SessionLocal()
    # try:
    #     # Check if the table exists
    #     db.execute(text('SELECT 1'))
    # except OperationalError:
    #     # If the table doesn't exist, create it
    #     create_table()
    
    try:
        yield db
    finally:
        db.close()