# models.py

from sqlalchemy import Column, Integer, String, Float, Date, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeatherEntry(Base):
    __tablename__ = 'weather_entries'

    id = Column(Integer, primary_key=True)
    town = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    temperature = Column(Float, nullable=False)
    cloud_cover = Column(String(50), nullable=False)
