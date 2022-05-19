import urllib.request
import json
from datetime import datetime

from .models import Weather

apiKey = None
base_url = None


def configure_request(app):
    global apiKey, base_url
    apiKey = app.config['WEATHER_API_KEY']
    base_url = app.config['WEATHER_API_BASE_URL']


def get_forecast(lat, lon):
    '''
    Function that gets the json response to our url request
    '''
    get_forecast_url = base_url.format(lat, lon, apiKey)

    with urllib.request.urlopen(get_forecast_url) as url:
        get_forecast_data = url.read()
        get_forecast_response = json.loads(get_forecast_data)

        weather_object = None

        if get_forecast_response:
            lat = get_forecast_response.get('lat')
            lon = get_forecast_response.get('lon')

            # City Names
            if lat == -0.1022 and lon == 34.7617:
                name = "Kisumu"
            elif lat == -4.0547 and lon == 39.6636:
                name = "Mombasa"
            elif lat == -3.2175 and lon == 40.11911:
                name = "Malindi"
            elif lat == -0.5273 and lon == 34.4571:
                name = "Homabay"
            elif lat == -3.6305 and lon == 39.8499:
                name = "Kilifi"
            elif lat == -2.2717 and lon == 40.902:
                name = "Lamu"
            elif lat == 0.2386 and lon == 34.2694:
                name = "Bondo"
            elif lat == 3.5833 and lon == 36.1167:
                name = "Turkana"
            elif lat == 0.4601 and lon == 34.117:
                name = "Busia"

            # Current
            current_timestamp = get_forecast_response['current'].get('dt')
            current_temp = get_forecast_response['current'].get('temp')
            current_feels_like = get_forecast_response['current'].get('feels_like')
            current_pressure = get_forecast_response['current'].get('pressure')
            current_humidity = get_forecast_response['current'].get('humidity')
            current_clouds = get_forecast_response['current'].get('clouds')
            current_visibility = get_forecast_response['current'].get('visibility')
            current_wind_speed = get_forecast_response['current'].get('wind_speed')
            current_wind_deg = get_forecast_response['current'].get('wind_deg')
            current_weather_id = get_forecast_response['current']['weather'][0].get('id')
            current_weather_main = get_forecast_response['current']['weather'][0].get('main')
            current_weather_description = get_forecast_response['current']['weather'][0].get('description')
            current_weather_icon = get_forecast_response['current']['weather'][0].get('icon')

            # Daily
            daily_timestamp = get_forecast_response['daily'].get('dt')
            daily_day_temp = get_forecast_response['daily']['temp'].get('day')
            daily_night_temp = get_forecast_response['daily']['temp'].get('night')
            daily_min_temp = get_forecast_response['daily']['temp'].get('min')
            daily_max_temp = get_forecast_response['daily']['temp'].get('max')
            daily_eve_temp = get_forecast_response['daily']['temp'].get('eve')
            daily_morn_temp = get_forecast_response['daily']['temp'].get('morn')
            daily_pressure = get_forecast_response['daily'].get('pressure')
            daily_humidity = get_forecast_response['daily'].get('humidity')
            daily_wind_speed = get_forecast_response['daily'].get('wind_speed')
            daily_wind_deg = get_forecast_response['daily'].get('wind_deg')
            daily_pop = get_forecast_response['daily'].get('pop')
            daily_rain = get_forecast_response['daily'].get('rain')
            daily_clouds = get_forecast_response['daily'].get('clouds')
            daily_weather_id = get_forecast_response['daily']['weather'][0].get('id')
            daily_weather_main = get_forecast_response['daily']['weather'][0].get('main')
            daily_weather_description = get_forecast_response['daily']['weather'][0].get('description')
            daily_weather_icon = get_forecast_response['daily']['weather'][0].get('icon')

            # Get current Time
            current_time = datetime.utcfromtimestamp(
                current_timestamp).strftime('%A %d %B, %Y %I:%M:%S %Z UTC')
            # Get Daily Prediction Time
            daily_time = datetime.utcfromtimestamp(
                daily_timestamp).strftime('%A %d %B, %Y %I:%M:%S %Z UTC')

            # Get current Status
            if current_weather_main == 'Clouds' or current_weather_description == 'light rain' or current_weather_description == 'overcast clouds':
                current_status = "go fish"
            else:
                current_status = "Not the best weather, better do something else with your time"

            # Get Daily Status
            if daily_weather_main == 'Clouds' or daily_weather_description == 'light rain' or daily_weather_description == 'overcast clouds':
                daily_status = "go fish"
            else:
                daily_status = "Not the best weather, better do something else with your time"

            weather_object = Weather(name, current_time, current_temp, current_feels_like, current_pressure, current_humidity,
                                     current_clouds, current_visibility, current_wind_speed, current_wind_deg, current_weather_id, current_weather_main,
                                     current_weather_description, current_weather_icon, current_status, daily_time, daily_day_temp, daily_night_temp,
                                     daily_min_temp, daily_max_temp, daily_eve_temp, daily_morn_temp, daily_pressure, daily_humidity, daily_wind_speed,
                                     daily_wind_deg, daily_weather_id, daily_weather_main, daily_weather_description, daily_weather_icon, daily_clouds,
                                     daily_pop, daily_rain, daily_status)

    return weather_object
