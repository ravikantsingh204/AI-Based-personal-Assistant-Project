import requests

def get_weather_forecast(city, api_key):
    base_url = "http://api.weatherstack.com/forecast"
    params = {
        "access_key": api_key,
        "query": city,
        "forecast_days": 3  # Limit to 3 days
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200 and "forecast" in data:
        print(f"Weather forecast for {city}:")
        for date, details in data["forecast"].items():
            print(f"{date}: High: {details['maxtemp']}°C, Low: {details['mintemp']}°C")
    else:
        print("Error:", data.get("error", {}).get("info", "Unable to fetch weather data"))

# Example usage
API_KEY = "3b6331393c5bc9b3dd21a41f730f09d9"
get_weather_forecast("New York", API_KEY)
