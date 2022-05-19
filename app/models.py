from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'


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

