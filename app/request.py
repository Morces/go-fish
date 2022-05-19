import urllib.request, json
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

            # Hourly
            for hourly_response in get_forecast_response['hourly']:
                hourly_timestamp = hourly_response.get('dt')
                hourly_temp = hourly_response.get('temp')
                hourly_feels_like= hourly_response.get('temp')
                hourly_pressure = hourly_response.get('pressure')
                hourly_humidity = hourly_response.get('humidity')
                hourly_clouds = hourly_response.get('clouds')
                hourly_visibility = hourly_response.get('visibility')
                hourly_wind_speed = hourly_response.get('wind_speed')
                hourly_wind_deg = hourly_response.get('wind_deg')
                hourly_wind_gust = hourly_response.get('wind_gust')
                hourly_weather_main = hourly_response['weather'][0].get('main')
                hourly_weather_description = hourly_response['weather'][0].get('description')
                hourly_weather_icon = hourly_response['weather'][0].get('icon')
                hourly_pop = hourly_response.get('pop')
               


            # Daily
            for response in get_forecast_response['daily']:
                daily_timestamp = response.get('dt')
                daily_day_temp = response['temp'].get('day')
                daily_night_temp = response['temp'].get('night')
                daily_min_temp = response['temp'].get('min')
                daily_max_temp = response['temp'].get('max')
                daily_eve_temp = response['temp'].get('eve')
                daily_morn_temp = response['temp'].get('morn')
                daily_pressure = response.get('pressure')
                daily_humidity = response.get('humidity')
                daily_wind_speed = response.get('wind_speed')
                daily_wind_deg = response.get('wind_deg')
                daily_pop = response.get('pop')
                daily_rain = response.get('rain')
                daily_clouds = response.get('clouds')
                daily_weather_id = response['weather'][0].get('id')
                daily_weather_main = response['weather'][0].get('main')
                daily_weather_description = response['weather'][0].get('description')
                daily_weather_icon = response['weather'][0].get('icon')

            # Get current Time
            current_time = datetime.utcfromtimestamp(current_timestamp).strftime('%A %d %B, %Y %I:%M:%S %Z')
            # Get Daily Prediction Time
            daily_time = datetime.utcfromtimestamp(daily_timestamp).strftime('%A %d %B, %Y %I:%M:%S %Z')

            # Get hourly Prediction Time
            hourly_time = datetime.utcfromtimestamp(hourly_timestamp).strftime('%A %d %B, %Y %I:%M:%S %Z')

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

             # Get Daily Status
            if hourly_weather_main == 'Clouds' or hourly_weather_description == 'light rain' or hourly_weather_description == 'overcast clouds':
                hourly_status = "go fish"
            else:
                hourly_status = "Not the best weather, better do something else with your time"



            # City Names
            name = ''
            if lat == -0.1022 and lon == 34.7617:
                name = "Kisumu"
            elif lat == -4.0547 and lon == 39.6636:
                name = "Mombasa"
            elif lat == -3.2175 and lon == 40.1191:
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
            
           

    weather_object = Weather(name, current_time, current_temp, current_feels_like, current_pressure, current_humidity,
                            current_clouds, current_visibility, current_wind_speed, current_wind_deg, current_weather_id, current_weather_main,
                            current_weather_description, current_weather_icon, current_status, daily_time, daily_day_temp, daily_night_temp,
                            daily_min_temp, daily_max_temp, daily_eve_temp, daily_morn_temp, daily_pressure, daily_humidity, daily_wind_speed,
                            daily_wind_deg, daily_weather_id, daily_weather_main, daily_weather_description, daily_weather_icon, daily_clouds,
                            daily_pop, daily_rain, daily_status, hourly_time, hourly_temp, hourly_feels_like,
                            hourly_pressure, hourly_humidity, hourly_clouds, hourly_visibility, hourly_wind_speed, hourly_wind_deg,
                            hourly_wind_gust, hourly_weather_main, hourly_weather_description, hourly_weather_icon, hourly_pop,hourly_status)

    print(name)
    return weather_object
