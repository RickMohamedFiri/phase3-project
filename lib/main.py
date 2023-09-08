# main.py

import argparse
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, WeatherEntry

engine = create_engine('sqlite:///weather.db')
Session = sessionmaker(bind=engine)

def create_database():
    Base.metadata.create_all(engine)
    print("Database created.")

def populate_database():
    session = Session()
    towns = ["Nairobi", "Mombasa", "Kisumu", "Eldoret", "Nakuru", "Meru", "Thika", "Kakamega", "Kericho", "Malindi"]
    
    # Generate random weather data for each town
    for town in towns:
        date = datetime(2023, 8, 1)
        end_date = datetime(2023, 8, 31)
        
        while date <= end_date:
            time = date.strftime("%H:%M:%S")
            temperature = random.randint(15, 35)  # Random temperature between 15°C and 35°C
            cloud_cover = random.choice(["Clear", "Partly Cloudy", "Cloudy", "Rainy"])
            
            entry = WeatherEntry(town=town, date=date.strftime("%Y-%m-%d"), time=time,
                                 temperature=temperature, cloud_cover=cloud_cover)
            session.add(entry)
            
            date += timedelta(hours=2)  # Increment date by 2 hours
        
    session.commit()
    print("Weather data populated.")

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
