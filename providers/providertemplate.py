# class TEMPLATE:
#Notes:
    #parameters and headers must be adjusted according to your planned API platform - see vendor documentation for requirements
#     def __init__(self, lat, lon, dt, airport):
#         self.lat = lat
#         self.lon = lon
#         self.dt = dt
#         self.airport=airport
#
#     def get_weather(self):
#         """api call & get request for TEMPLATE platform"""
#         api_url = os.getenv('TEMPLATE_URL' - replace with URL in .env file)
#         api_key = os.getenv('TEMPLATE_KEY - replace with key in .env file')
#         weather_request = requests.get(url=api_url,
#                                        params={'lat': self.lat,
#                                                'lon': self.lon,
#                                                'start': self.dt,
#                                                'end': self.dt,
#                                                 },
#                                        headers={
#                                                "x-rapidapi-key": TEMPLATE_KEY,
#                                                "x-rapidapi-host": "TEMPLATE_URL",
#                                                "Content-Type": "application/json"
#                                        })
#         TEMPLATE_DATA = weather_request.json()
#         return TEMPLATE_DATA
#
#     def normalize(self, TEMPLATE_DATA):
#         """plugs data into a standardized format that can be crossed between api platforms."""
#         #Note: These dictionary parameters must be adjusted based on your API platform's json data.
#         return {
#             "source": "weatherapi",
#             "location": self.airport,
#             "date": self.dt,
#             "avg_temp_f": meteostat_data["data"][0]['tavg'],
#             "max_temp_f": meteostat_data['data'][0]['tmax'],
#             "min_temp_f": meteostat_data['data'][0]['tmin'],
#             "precipitation_in": meteostat_data['data'][0]['prcp'],
#             "wind_mph": meteostat_data['data'][0]['wspd']
#         }