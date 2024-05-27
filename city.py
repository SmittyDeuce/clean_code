class City:
    def __init__(self, name, temperature, condition, humidity):
        
        self.name = name
        self.temperature = int(temperature)
        self.condition= condition
        self.humidity = int(humidity)

    def city_details(self):
        return (f"City: {self.name}\n"
                f"Temperature: {self.temperature}\n"
                f"Condition: {self.condition}\n"
                f"Humidity: {self.humidity}%")

nyc = City("New York City", 70, "Sunny",50)

print(nyc.city_details())