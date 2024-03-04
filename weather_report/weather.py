import requests

def get_location():
  location = input("Enter city name or zip code: ")
  return location

def fetch_weather(location, api_key):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
  response = requests.get(url)
  return response.json()

def extract_weather_data(data):
  try:
    temperature = data["main"]["temp"] - 273.15 
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
  except KeyError:
    return None

  return {
      "temperature": temperature,
      "humidity": humidity,
      "wind_speed": wind_speed,
      "description": description
  }

def display_weather(weather_data):
  if weather_data is None:
    print("Error: Could not retrieve weather data.")
  else:
    print(f"Location: {location}")
    print(f"Temperature: {weather_data['temperature']:.2f} °C")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    print(f"Description: {weather_data['description']}")

if __name__ == "__main__":
  api_key = "d730783e37ff0e92c9764d812d1a46f0" 
  location = get_location()
  weather_data = extract_weather_data(fetch_weather(location, api_key))
  display_weather(weather_data)
