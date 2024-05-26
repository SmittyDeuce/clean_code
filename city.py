class City:
    def __init__(self, name, temperature, weather, humidity):
        
        self.name = name
        self.temperature = int(temperature)
        self.weather = weather
        self.humidity = int(humidity)

    def fetch_weather_data(self):

        return f"City: {self.name}\nTemp: {self.temperature}\nWeather: {self.weather}\nHumidity: {self.humidity}"
    

nyc = City("New York City", 70, "Sunny",50)

print(nyc.fetch_weather_data())