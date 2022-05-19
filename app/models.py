class Weather:
    '''
    Current Forecast class to define forecast Objects
    '''

    def __init__(self, name,current_time, current_temp, current_feels_like,
                 current_pressure, current_humidity, current_clouds, current_visibility,
                 current_wind_speed, current_wind_deg, current_weather_id, current_weather_main,
                 current_weather_description, current_weather_icon, current_status, daily_time, daily_day_temp, daily_night_temp,
                 daily_min_temp, daily_max_temp, daily_eve_temp, daily_morn_temp, daily_pressure,
                 daily_humidity, daily_wind_speed, daily_wind_deg, daily_weather_id,
                 daily_weather_main, daily_weather_description, daily_weather_icon,
                 daily_clouds, daily_pop, daily_rain, daily_status):
                 
        self.name = name

        # Current
        self.current_time = current_time
        self.current_temp = current_temp
        self.current_feels_like = current_feels_like
        self.current_pressure = current_pressure
        self.current_humidity = current_humidity
        self.current_clouds = current_clouds
        self.current_visibility = current_visibility
        self.current_wind_speed = current_wind_speed
        self.current_wind_deg = current_wind_deg
        self.current_weather_id = current_weather_id
        self.current_weather_main = current_weather_main
        self.current_weather_description = current_weather_description
        self.current_weather_icon = current_weather_icon
        self.current_status = current_status

        # Daily
        self.daily_time = daily_time
        self.daily_day_temp = daily_day_temp
        self.daily_night_temp = daily_night_temp
        self.daily_min_temp = daily_min_temp
        self.daily_max_temp = daily_max_temp
        self.daily_eve_temp = daily_eve_temp
        self.daily_morn_temp = daily_morn_temp
        self.daily_pressure = daily_pressure
        self.daily_humidity = daily_humidity
        self.daily_wind_speed = daily_wind_speed
        self.daily_wind_deg = daily_wind_deg
        self.daily_weather_id = daily_weather_id
        self.daily_weather_main = daily_weather_main
        self.daily_weather_description = daily_weather_description
        self.daily_weather_icon = daily_weather_icon
        self.daily_clouds = daily_clouds
        self.daily_pop = daily_pop
        self.daily_rain = daily_rain
        self.daily_status = daily_status

