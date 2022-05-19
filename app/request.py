import urllib.request, json
from datetime import datetime


from .models import CurrentForecast, DailyForecast


# Getting api key
apiKey=None

# Getting the base url
base_url=None

def configure_request(app):
  global apiKey, base_url
  apiKey=app.config['WEATHER_API_KEY']
  base_url=app.config['WEATHER_API_BASE_URL']


def get_current_forecast(lat, lon):
    '''
    Function that gets the json response to our url request
    '''
    get_forecast_url = base_url.format(lat, lon, apiKey)

    with urllib.request.urlopen(get_forecast_url) as url:
        get_forecast_data = url.read()
        get_forecast_response = json.loads(get_forecast_data)

        current_forecast = None
        

        if get_forecast_response['current']:
            current_forecast_object = get_forecast_response['current']
            current_forecast = process_current_results(current_forecast_object)
           

    return current_forecast

def process_current_results(current_forecast_object):
    '''
    Function that processes the current forecast result and 
    transforms them to a list of Objects

    Args:
      current_forecast_list: A list of dictionaries that contain current 
      details

    Returns:
      forecast_results_current: A list of current forecast objects
    '''
    

    if current_forecast_object:

        timestamp = current_forecast_object.get('dt')
        temp = current_forecast_object.get('temp')
        feels_like = current_forecast_object.get('feels_like')
        pressure = current_forecast_object.get('pressure')
        humidity = current_forecast_object.get('humidity')
        clouds = current_forecast_object.get('clouds')
        visibility = current_forecast_object.get('visibility')
        wind_speed = current_forecast_object.get('wind_speed')
        wind_deg = current_forecast_object.get('wind_deg')
        weather_id = current_forecast_object['weather'][0].get('id')
        weather_main = current_forecast_object['weather'][0].get('main')
        weather_description = current_forecast_object['weather'][0].get('description')
        weather_icon = current_forecast_object['weather'][0].get('icon')
        
        if weather_main == 'Clouds' or weather_description == 'light rain' or weather_description == 'overcast clouds':
          status="go fish"
        else:
          status="Not the best weather, better do something else with your time"
          
       
        time= datetime.utcfromtimestamp(timestamp).strftime('%A %d %B, %Y %I:%M:%S %Z UTC')
        
        current_forecast = CurrentForecast(time, temp, feels_like, pressure, humidity, clouds,
                                                  visibility, wind_speed, wind_deg, weather_id, weather_main,
                                                  weather_description, weather_icon, status=status)

        print(status)
    
    return current_forecast


def get_daily_forecast(lat, lon):
    '''
    Function that gets the json response to our url request
    '''
    get_forecast_url = base_url.format(lat, lon, apiKey)

    with urllib.request.urlopen(get_forecast_url) as url:
        get_forecast_data = url.read()
        get_forecast_response = json.loads(get_forecast_data)

        if get_forecast_response['daily']:
            daily_forecast_list = get_forecast_response['daily']
            forecast_results_daily = process_daily_results(daily_forecast_list)

    return  forecast_results_daily


def process_daily_results(daily_forecast_list):
    '''
    Function that processes the daily forecast result and 
    transforms them to a list of Objects

    Args:
      daily_forecast_list: A list of dictionaries that contain daily 
      details

    Returns:
      forecast_results_daily: A list of daily forecast objects
    '''
    forecast_results_daily = []

    for daily_result in daily_forecast_list:

        timestamp = daily_result.get('dt')
        day_temp = daily_result['temp'].get('day')
        night_temp = daily_result['temp'].get('night')
        min_temp = daily_result['temp'].get('min')
        max_temp = daily_result['temp'].get('max')
        eve_temp = daily_result['temp'].get('eve')
        morn_temp = daily_result['temp'].get('morn')
        pressure = daily_result.get('pressure')
        humidity = daily_result.get('humidity')
        wind_speed = daily_result.get('wind_speed')
        wind_deg = daily_result.get('wind_deg')
        pop = daily_result.get('pop')
        rain = daily_result.get('rain')
        clouds = daily_result.get('clouds')
        weather_id = daily_result['weather'][0].get('id')
        weather_main = daily_result['weather'][0].get('main')
        weather_description = daily_result['weather'][0].get('description')
        weather_icon = daily_result['weather'][0].get('icon')

        if weather_main == 'Clouds' or weather_description == 'light rain' or weather_description == 'overcast clouds':
          status="go fish"
        else:
          status="Not the best weather, better do something else with your time"
          
        
        time= datetime.utcfromtimestamp(timestamp).strftime('%A %d %B, %Y %I:%M:%S %Z UTC')
        
        
        daily_forecast_object = DailyForecast(time, day_temp,
                                              night_temp, min_temp, max_temp, eve_temp, morn_temp,
                                              pressure, humidity, wind_speed, wind_deg,
                                              weather_id, weather_main, weather_description,
                                              weather_icon, clouds, pop, rain, status)

        forecast_results_daily.append(daily_forecast_object)
   
    return forecast_results_daily
