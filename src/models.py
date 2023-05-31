from sqlalchemy import String, Integer
from sqlalchemy.sql.schema import Column
from database import Base

schema = "public"

class Event(Base):
    __tablename__ = "Events"
    __table_args__ = {"schema": schema}

    id = Column('id', Integer, primary_key=True)
    title = Column('title',String, nullable=False)
    desc = Column('desc',String, nullable=False)
