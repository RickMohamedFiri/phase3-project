# main.py

import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, WeatherEntry

engine = create_engine('sqlite:///weather.db')
Session = sessionmaker(bind=engine)

def create_database():
    Base.metadata.create_all(engine)
    print("Database created.")

def populate_database():
    # Code to populate the database with weather data
    pass

def list_weather_entries(town, date):
    session = Session()
    entries = session.query(WeatherEntry).filter_by(town=town, date=date).all()
    
    if entries:
        print(f"Weather data for {town} on {date}:")
        for entry in entries:
            print(f"Time: {entry.time}, Temperature: {entry.temperature}, Cloud Cover: {entry.cloud_cover}")
    else:
        print(f"No weather data found for {town} on {date}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Weather App")
    parser.add_argument("command", choices=["create", "populate", "list"], help="Command to execute")

    args = parser.parse_args()

    if args.command == "create":
        create_database()
    elif args.command == "populate":
        populate_database()
    elif args.command == "list":
        town = input("Enter the town: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        list_weather_entries(town, date)
