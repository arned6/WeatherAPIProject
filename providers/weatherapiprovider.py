import os
import requests
from dotenv import load_dotenv


load_dotenv()

class WeatherApiProvider:
    def __init__(self, lat=0.0, lon=0.0, dt="", airport=""):
        self.lat = lat
        self.lon = lon
        self.dt = dt
        self.airport = airport

    def get_weather(self):
        """api call & get request for weatherapi platform"""
        api_url = os.getenv('WEATHER_API_URL')
        api_key = os.getenv('WEATHER_API_KEY')
        weather_request = requests.get(url=api_url,
                                       params={'q': f"{self.lat},{self.lon}",
                                               'dt': self.dt,
                                               'key': api_key
                                               })
        weatherapi_data = weather_request.json()
        return weatherapi_data
    def normalize(self, weatherapi_data):
        """plugs data into a standardized format that can be crossed between api platforms."""
        return {
            "source": "weatherapi",
            "location": self.airport,
            "date": self.dt,
            "avg_temp_f": weatherapi_data["forecast"]["forecastday"][0]["day"]["avgtemp_f"],
            "max_temp_f": weatherapi_data['forecast']['forecastday'][0]['day']["maxtemp_f"],
            "min_temp_f": weatherapi_data['forecast']['forecastday'][0]['day']["mintemp_f"],
            "precipitation_in": weatherapi_data['forecast']['forecastday'][0]['day']["totalprecip_in"],
            "wind_mph": weatherapi_data['forecast']['forecastday'][0]['day']["maxwind_mph"],
        }




