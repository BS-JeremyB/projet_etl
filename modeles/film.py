from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)

class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    rating = Column(Float)
    overview = Column(String)
