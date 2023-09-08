# main.py

import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, WeatherEntry
from datetime import datetime

engine = create_engine('sqlite:///weather.db')
Session = sessionmaker(bind=engine)

def create_database():
    Base.metadata.create_all(engine)
    print("Database created.")

from datetime import time  # Add this import

# ...

def populate_database():
    session = Session()
    data = [
        {
            "town": "Nairobi",
            "date": datetime(2023, 8, 1),
            "time": time(0, 0, 0),  # Use a Python time object
            "temperature": 23.6,
            "cloud_cover": "Windy",
        }
        # Add more data as needed
    ]

    for entry_data in data:
        entry = WeatherEntry(**entry_data)
        session.add(entry)

    session.commit()
    print("Weather data populated.")


def list_weather_entries(town, date):
    session = Session()
    entries = session.query(WeatherEntry).filter_by(town=town, date=date).all()
    
    if entries:
        print(f"Weather data for {town} on {date}:")
        for entry in entries:
            print(f"Time: {entry.time.strftime('%H:%M:%S')}, Temperature: {entry.temperature}, Cloud Cover: {entry.cloud_cover}")
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
