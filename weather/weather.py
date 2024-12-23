import requests

def get_weather_forecast(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            print(f"Weather forecast for {city}:")
            for forecast in data['list'][:5]:  # Limit to 5 time slots
                time = forecast['dt_txt']
                temp = forecast['main']['temp']
                description = forecast['weather'][0]['description']
                print(f"{time}: {temp}°C, {description.capitalize()}")
        else:
            print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
API_KEY = "546580cd453b756fff4729ff66358530"
city_name = "New York"
get_weather_forecast(city_name, API_KEY)
