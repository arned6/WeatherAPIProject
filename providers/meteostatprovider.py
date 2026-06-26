import os
import requests
from dotenv import load_dotenv
load_dotenv()

class MeteoStatProvider:
    def __init__(self, lat=0.0, lon=0.0, dt="", airport=""):
        self.lat = lat
        self.lon = lon
        self.dt = dt
        self.airport=airport

    def get_weather(self):
        """api call & get request for meteostat platform"""
        api_url = os.getenv('METEOSTAT_URL_DAILY')
        api_key = os.getenv('METEOSTAT_KEY')
        weather_request = requests.get(url=api_url,
                                       params={'lat': self.lat,
                                               'lon': self.lon,
                                               'start': self.dt,
                                               'end': self.dt,
                                               'units':"imperial"
                                                },
                                       headers={
                                               "x-rapidapi-key": api_key,
                                               "x-rapidapi-host": "meteostat.p.rapidapi.com",
                                               "Content-Type": "application/json"
                                       })
        meteostat_data = weather_request.json()
        return meteostat_data

    def normalize(self, meteostat_data):
        """plugs data into a standardized format that can be crossed between api platforms."""
        return {
            "source": "meteostat",
            "location": self.airport,
            "date": self.dt,
            "avg_temp_f": meteostat_data["data"][0]['tavg'],
            "max_temp_f": meteostat_data['data'][0]['tmax'],
            "min_temp_f": meteostat_data['data'][0]['tmin'],
            "precipitation_in": meteostat_data['data'][0]['prcp'],
            "wind_mph": meteostat_data['data'][0]['wspd']
        }