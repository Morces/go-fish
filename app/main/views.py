from flask import render_template

from . import main
from ..request import get_current_forecast, get_daily_forecast, get_city_name

# Views


@main.route('/')
def index():
    '''
    view root page function that returns the index page
    and its data
    '''
    
    title = 'Home'
    
    ksm_current = get_current_forecast(-0.1022, 34.7617)
    ksm_daily_results = get_daily_forecast(-0.1022, 34.7617)
    city_name = get_city_name(-0.1022, 34.7617)
    
    

    msa_current = get_current_forecast(-4.0547, 39.6636)
    msa_daily_results = get_daily_forecast(-4.0547, 39.6636)

    malindi_current = get_current_forecast( -3.2175, 40.1191)
    malindi_daily_results = get_daily_forecast(-3.2175, 40.1191)

    homabay_current = get_current_forecast(-0.5273, 34.4571)
    homabay_daily_results = get_daily_forecast(-0.5273, 34.4571)

    kilifi_current = get_current_forecast(-3.6305, 39.8499)
    kilifi_daily_results = get_daily_forecast(-3.6305, 39.8499)

    lamu_current = get_current_forecast(-2.2717, 40.902)
    lamu_daily_results = get_daily_forecast(-2.2717, 40.902)

    bondo_current = get_current_forecast(0.2386, 34.2694)
    bondo_daily_results = get_daily_forecast(0.2386, 34.2694)

    turkana_current = get_current_forecast(3.5833, 36.1167)
    turkana_daily_results = get_daily_forecast(3.5833, 36.1167)

    busia_current = get_current_forecast(0.4601, 34.117)
    busia_daily_results = get_daily_forecast(0.4601, 34.117)
    
    current_cities=[ksm_current, malindi_current, homabay_current, kilifi_current, bondo_current, turkana_current, busia_current, msa_current, lamu_current]
    daily_cities=[ksm_daily_results, malindi_daily_results, homabay_daily_results, kilifi_daily_results, bondo_daily_results, turkana_daily_results, busia_daily_results, msa_daily_results, lamu_daily_results]
    
  
    return render_template('index.html', title=title, current_cities=current_cities, daily_cities=daily_cities, city_name=city_name)

