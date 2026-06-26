#master import list
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from providers.weatherapiprovider import WeatherApiProvider
from providers.meteostatprovider import MeteoStatProvider
from comparator.comparator import Comparator
from reporting.reportengine import ReportingEngine

location_data={}

#Load all of the information from the config file into variable location_data
with open("config/config.json", "r") as file:
        json_file_contents = file.read()
        location_data = json.loads(json_file_contents)

#pull datetime for previous date
yesterday = date.today() - timedelta(days=1)

#scrape location_data dictionary for list of currently programmed airport codes
airport_list = [] 
for key in location_data:
    airport_list.append(location_data[key]['code'])

#Provides user with available input list
print (f"Current List of available airports: {", ".join(airport_list)}")

def airport_input():
    """Prompt user for airport select, validate selection against existing config.json"""
    airport=input("Please type a three-letter code from the list above: \n")
    if airport not in airport_list:
        print("Please select a valid airport.")
        airport_input()
    else:
        print (f"You have selected {airport}. Thank you!")
        return airport

airport_code=airport_input()
#Cut irrelevant json data from location_data
for location in location_data.values():
    if location['code'] == airport_code:
        location_data=location
        #Create lat and lon variables from filtered location_data
        latitude = location_data['latitude']
        longitude = location_data['longitude']
        print(f"Your airport information is:\n"
              f"Airport Code: {airport_code}\n"
              f"Latitude: {location_data['latitude']}\n"
              f"Longitude: {location_data['longitude']}\n")

#Load in API Provider #1 from weatherapiprovider.py
WeatherAPI=WeatherApiProvider(lat=latitude,lon=longitude,airport=airport_code, dt=yesterday)
# d1=(WeatherAPI.normalize(WeatherAPI.get_weather()))

#Load in API Provider #2 from weatherapiprovider.py
MeteoStat=MeteoStatProvider(lat=latitude,lon=longitude,airport=airport_code, dt=yesterday)
# d2=(MeteoStat.normalize(MeteoStat.get_weather()))

with ThreadPoolExecutor(max_workers=2) as executor:
    future1 = executor.submit(
        lambda: WeatherAPI.normalize(WeatherAPI.get_weather())
    )
    future2 = executor.submit(
        lambda: MeteoStat.normalize(MeteoStat.get_weather())
    )
    weatherapi_data=future1.result()
    meteostat_data=future2.result()


#Load in Comparator Class and compare data
StatComparator = Comparator(d1=weatherapi_data, d2=meteostat_data)
compared_data = StatComparator.comparison()


#Load in Report Output Class
Report = ReportingEngine(d1=weatherapi_data, d2=meteostat_data, compare=compared_data, date=yesterday, location=location['code'])
#Run Drift detection report
Report.driftdetect()
Report.csvpost()

print("File can be found in outputs/output.csv.")