from city import City


class WeatherParser:
    def parse_weather_data(self,city):
        if not city:
            return "Weather data not available"
        
        city_name = city.name
        temperature = city.temperature
        condition = city.condition
        humidity = city.humidity
        return f"Weather in {city_name}: {temperature} degrees, {condition}, Humidity: {humidity}%"