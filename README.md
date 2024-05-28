# clean_code

# Weather Forecast Application

This Python application fetches weather data for cities and provides basic and detailed forecasts.Split into 6 modules to organize the code and improve maintainability.

## Modules

### `city.py`

This module defines the `City` class, which represents a city and its weather attributes such as name, temperature, condition, and humidity. It also provides a method `city_details` to format and return these details as a string.

### `weather_fetcher.py`

The `WeatherFetcher` class in this module fetches weather data for a given city name. It simulates fetching data from a predefined dictionary and returns a `City` object initialized with the fetched weather data.

### `weather_parser.py`

The `WeatherParser` class in this module parses weather data for a given `City` object. It extracts the city's attributes (name, temperature, condition, humidity) and formats them into a human-readable string representing the weather information.

### `weather_app.py`

This module contains the `WeatherApp` class, which serves as the main component of the application. It interacts with the user, fetches and parses weather data using instances of `WeatherFetcher` and `WeatherParser`, and provides basic and detailed forecasts.

- `WeatherApp`: Initializes instances of `WeatherFetcher` and `WeatherParser` and provides methods to fetch weather data, display basic and detailed forecasts, and run the main application loop.

### `main.py`

The `main.py` module is the entry point of the application. It creates an instance of `WeatherApp` and calls its `main` method to start the application.
