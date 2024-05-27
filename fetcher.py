from city import City

class WeatherFetcher:
    def fetch_weather_data(self, city_name):
        print(f"Fetching weather data for {city_name}...")
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        data = weather_data.get(city_name)
        if data:
            return City(city_name, data["temperature"], data["condition"], data["humidity"])
        return None