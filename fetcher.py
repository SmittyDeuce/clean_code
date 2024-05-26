from city import City

class WeatherFetcher:
    def fetch_data(self,city_name):

        print(f"Fetching weather data for {city_name}...")
        # Simulated data based on city
        weather_data = {}
            
        return weather_data.get(city_name, {})
