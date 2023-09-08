from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class WeatherEntry(Base):
    __tablename__ = 'weather_entries'

    id = Column(Integer, primary_key=True)
    town = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    temperature = Column(Integer, nullable=False)
    cloud_cover = Column(String)

    def __init__(self, town, date, temperature, cloud_cover):
        self.town = town
        self.date = date
        self.temperature = temperature
        self.cloud_cover = cloud_cover

# Add any other models you need below this line

# Example of another model:
# class AnotherModel(Base):
#     __tablename__ = 'another_table'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)

# Replace 'sqlite:///weather.db' with your database connection string
engine = create_engine('sqlite:///weather.db')

Base.metadata.create_all(engine)
