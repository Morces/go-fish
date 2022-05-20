from flask import render_template
from flask_login import login_required

from . import main
from ..request import get_current_forecast, get_daily_forecast, get_hourly_forecast

# Views
@main.route('/')
def index():
  '''
  view root page function that returns the home page
  and its data
  '''
  return render_template('index.html')


@main.route('/gofishing')
@login_required
def gofish():
    '''
    view root page function that returns the home page
    and its data
    '''
    
    title = 'Weather Forecasts'
    
    current_kisumu = get_current_forecast(-0.1022, 34.7617)
    hourly_kisumu = get_hourly_forecast(-0.1022, 34.7617)
    daily_kisumu = get_daily_forecast(-0.1022, 34.7617)

    current_mombasa = get_current_forecast(-4.0547, 39.6636)
    hourly_mombasa = get_hourly_forecast(-4.0547, 39.6636)
    daily_mombasa = get_daily_forecast(-4.0547, 39.6636)

    current_malindi = get_current_forecast(-3.2175, 40.1191)
    hourly_malindi = get_hourly_forecast(-3.2175, 40.1191)
    daily_malindi = get_daily_forecast(-3.2175, 40.1191)

    current_homabay = get_current_forecast(-0.5273, 34.4571)
    hourly_homabay = get_hourly_forecast(-0.5273, 34.4571)
    daily_homabay = get_daily_forecast(-0.5273, 34.4571)

  
    current_kilifi = get_current_forecast(-3.6305, 39.8499)
    hourly_kilifi = get_hourly_forecast(-3.6305, 39.8499)
    daily_kilifi = get_daily_forecast(-3.6305, 39.8499)


    current_lamu = get_current_forecast(-2.2717, 40.902)
    hourly_lamu = get_hourly_forecast(-2.2717, 40.902)
    daily_lamu = get_daily_forecast(-2.2717, 40.902)

    current_bondo = get_current_forecast(0.2386, 34.2694)
    hourly_bondo = get_hourly_forecast(0.2386, 34.2694)
    daily_bondo = get_daily_forecast(0.2386, 34.2694)

    current_turkana = get_current_forecast(3.5833, 36.1167)
    hourly_turkana = get_hourly_forecast(3.5833, 36.1167)
    daily_turkana = get_daily_forecast(3.5833, 36.1167)

    current_busia = get_current_forecast(0.4601, 34.117)
    hourly_busia = get_hourly_forecast(0.4601, 34.117)
    daily_busia = get_daily_forecast(0.4601, 34.117)
    
    current_cities = [current_kisumu, current_mombasa, current_malindi, current_homabay, current_kilifi, current_lamu, current_bondo, current_turkana, current_busia]
  
    return render_template('home.html', title=title, current_cities=current_cities, hourly_kisumu=hourly_kisumu, 
            hourly_mombasa=hourly_mombasa, hourly_malindi=hourly_malindi, hourly_homabay=hourly_homabay, hourly_kilifi=hourly_kilifi,
            hourly_lamu=hourly_lamu, hourly_bondo=hourly_bondo, hourly_turkana=hourly_turkana, hourly_busia=hourly_busia, 
            daily_kisumu=daily_kisumu, daily_mombasa=daily_mombasa, daily_malindi=daily_malindi, daily_homabay=daily_homabay, 
            daily_kilifi = daily_kilifi,daily_lamu=daily_lamu, daily_bondo=daily_bondo, daily_turkana=daily_turkana, daily_busia=daily_busia)
