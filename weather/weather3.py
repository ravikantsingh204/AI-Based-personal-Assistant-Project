import requests

def get_weather_forecast(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print("Unable to fetch weather data.")

# Example usage
get_weather_forecast("New Delhi")
