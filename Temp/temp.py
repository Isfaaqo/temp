import requests
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("API_KEY")  # Access the API_KEY variable



def get_weather(city):
    # API request to get current weather data
    current_weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(current_weather_url)

    if response.status_code == 200:
        data = response.json()
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f'\nCurrent Weather in {city}, {country}')
        print(f'Temperature: {temperature}°C')
        print(f'Weather: {weather_description}')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
        print()

        # API request to get hourly forecast data for the next 12 hours
        forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            print('Hourly Temperature Forecast for the Next 12 Hours (3-hour increments):')
            for item in forecast_data['list'][:4]:  # Next 12 hours, 3-hour increments
                timestamp = item['dt']
                temperature = item['main']['temp']
                weather_description = item['weather'][0]['description']
                timestamp_dt = datetime.utcfromtimestamp(timestamp)
                am_pm_time = timestamp_dt.strftime('%I:%M %p')  # Convert to AM/PM time format
                print(f'Time: {am_pm_time}, Temperature: {temperature}°C, Weather: {weather_description}')
        else:
            print(f'Error: Unable to fetch hourly forecast data for {city}')
    else:
        print(f'Error: Unable to fetch weather data for {city}')

if __name__ == "__main__":
    city_name = input("\nEnter city name: ")
    while city_name:
        get_weather(city_name)
        city_name = input("\nEnter city name: ")
        
    
