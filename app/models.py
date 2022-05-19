class CurrentForecast:
    '''
    Current Forecast class to define forecast Objects
    '''

    def __init__(self, time, temp, feels_like,
                 pressure, humidity, clouds, visibility,
                 wind_speed, wind_deg, weather_id, weather_main,
                 weather_description, weather_icon, status):
                 

        self.time = time
        self.temp = temp
        self.feels_like = feels_like
        self.pressure = pressure
        self.humidity = humidity
        self.clouds = clouds
        self.visibility = visibility
        self.wind_speed = wind_speed
        self.wind_deg = wind_deg
        self.weather_id = weather_id
        self.weather_main = weather_main
        self.weather_description = weather_description
        self.weather_icon = weather_icon
        self.status = status

        

class DailyForecast:
    '''
    Daily Forecast class to define forecast Objects
    '''

    def __init__(self, time, day_temp, night_temp,
                 min_temp, max_temp, eve_temp, morn_temp, pressure,
                 humidity, wind_speed, wind_deg, weather_id,
                 weather_main, weather_description, weather_icon,
                 clouds, pop, rain, status):

        self.time = time
        self.day_temp = day_temp
        self.night_temp = night_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.eve_temp = eve_temp
        self.morn_temp = morn_temp
        self.pressure = pressure
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.wind_deg = wind_deg
        self.weather_id = weather_id
        self.weather_main = weather_main
        self.weather_description = weather_description
        self.weather_icon = weather_icon
        self.clouds = clouds
        self.pop = pop
        self.rain = rain
        self.status = status
