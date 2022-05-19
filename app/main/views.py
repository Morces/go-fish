from flask import render_template

from . import main
from ..request import get_forecast

# Views


@main.route('/home')
def index():
    '''
    view root page function that returns the index page
    and its data
    '''
    
    title = 'Weather Forecasts'
    
    Kisumu = get_forecast(-0.1022, 34.7617)
    Mombasa = get_forecast(-4.0547, 39.6636)
    Malindi = get_forecast(-3.2175, 40.1191)
    Homabay = get_forecast(-0.5273, 34.4571)
    Kilifi = get_forecast(-3.6305, 39.8499)
    Lamu = get_forecast(-2.2717, 40.902)
    Bondo = get_forecast(0.2386, 34.2694)
    Turkana = get_forecast(3.5833, 36.1167)
    Busia = get_forecast(0.4601, 34.117)
    
    cities = [Kisumu, Mombasa, Malindi, Homabay, Kilifi, Lamu, Bondo, Turkana, Busia]
  
    return render_template('home.html', title=title, cities=cities)

