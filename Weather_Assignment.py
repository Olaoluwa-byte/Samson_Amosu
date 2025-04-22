import json
import requests  # Import the requests module
from datetime import datetime

API_KEY = ''  # Your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_data(lat, lon):
    """
    Fetch weather data from OpenWeatherMap API using latitude and longitude.
    
    Args:
    lat (float): Latitude of the location.
    lon (float): Longitude of the location.
    
    Returns:
    dict: JSON response from the API containing weather data.
    """
    try:
        params = {
            'lat': lat,
            'lon': lon,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def process_weather_data(data):
    """
    Process the raw weather data to extract relevant information.
    
    Args:
    data (dict): Raw JSON data from the API.
    
    Returns:
    dict: Processed data containing city, temperature, weather description, wind speed, and date.
    """
    try:
        city = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        processed_data = {
            'city': city,
            'temperature': temperature,
            'weather_description': weather_description.capitalize(),
            'wind_speed': wind_speed,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return processed_data
    except (KeyError, TypeError) as e:
        print(f"Error processing data: {e}")
        return None

def display_weather_data(processed_data):
    """
    Display the processed weather data.
    
    Args:
    processed_data (dict): Processed weather data.
    """
    print(f"Weather in {processed_data['city']} as of {processed_data['date']}:")
    print(f"Temperature: {processed_data['temperature']}°C")
    print(f"Weather: {processed_data['weather_description']}")
    print(f"Wind Speed: {processed_data['wind_speed']} m/s")

def main():
    """
    Main function to fetch and display weather data based on user input.
    """
    try:
        lat = float(input("Enter the latitude: "))
        lon = float(input("Enter the longitude: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for latitude and longitude.")
        return
    
    raw_data = get_weather_data(lat, lon)
    if raw_data:
        processed_data = process_weather_data(raw_data)
        if processed_data:
            display_weather_data(processed_data)

if __name__ == "__main__":
    main()
