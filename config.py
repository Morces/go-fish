import os

class Config:
  '''
  General configuration parent class
  '''
  WEATHER_API_BASE_URL='https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely&lang=en&units=metric&appid={}'
  WEATHER_API_KEY=os.environ.get('WEATHER_API_KEY')
  SECRET_KEY = '8DH89s8ej3'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wachira:Lydiah007@localhost/gofish'
  UPLOADED_PHOTOS_DEST ='app/static/photos'

  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = 'oneminutepitches@gmail.com'
  MAIL_PASSWORD = 'wakadinali'

class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
    Config: The parent configuration class with General
    configuration settings
  '''
  SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL').replace ('://', 'ql://', 1)  

class DevConfig(Config):
  '''
  Development configuration child class

  Args:
    Config: The parent configuration class with General 
    configuration settings
  '''

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wachira:Lydiah007@localhost/gofish'
  
DEBUG = True  

config_options = {
  'development': DevConfig,
  'production': ProdConfig
}
