import requests, os
from django.core.cache import cache

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather_data(city):
    cache_key =f"weather:{city.lower()}"
    cached = cache.get(cache_key)

    if cached:
        return cached
    
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    r = requests.get(url)
    if r.status_code !=200:
        return {'error' : 'Couldnt reach data from API.'}

    data = r.json()
    cache.set(cache_key, data, timeout=43200)
    return data


