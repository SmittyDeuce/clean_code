from weather_fetcher.py import WeatherFetcher
from weather_parser import WeatherParser


class WeatherApp:
    def __init(self):
        self.fetcher = WeatherFetcher()
        self.parser = WeatherParser()