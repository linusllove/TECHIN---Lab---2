import csv

csv_file_path = 'C:/Users/Julianne Li/Desktop/510/TECHIN---Lab---2/events.csv'

with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    columns = next(reader)
    print(columns)  

with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    locations = [row['location'] for row in reader if 'location' in row]
    print(locations)

import requests
import csv

with open('events.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    locations = [row['location'] for row in reader]

unique_locations = list(set(locations))

location_coordinates = {}
for location in unique_locations:
    if location and location != 'N/A': 
        geo_url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json"
        response = requests.get(geo_url)
        data = response.json()
        if data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            location_coordinates[location] = (lat, lon)

print(location_coordinates)


import requests

def get_weather(lat, lon):

    headers = {
        "User-Agent": "myweatherapp (contact@myweatherapp.com)"
    }


    points_url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(points_url, headers=headers)
    

    if response.status_code == 200:
        points_data = response.json()
        forecast_url = points_data["properties"]["forecast"]
        
    
        forecast_response = requests.get(forecast_url, headers=headers)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            
        
            for period in forecast_data["properties"]["periods"]:
                print(f"Time: {period['name']}")
                print(f"Temperature: {period['temperature']} {period['temperatureUnit']}")
                print(f"Wind: {period['windSpeed']} {period['windDirection']}")
                print(f"Forecast: {period['shortForecast']}\n")
        else:
            print("Failed to retrieve the forecast data.")
    else:
        print("Failed to retrieve the location data.")


latitude = "39.7456"
longitude = "-97.0892"


get_weather(latitude, longitude)
