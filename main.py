''' From my understanding of question 2 was to split the
methods into their own module for better reading and neater code
so I esentially copied them from the main and into their own
module if I was supposed to do more with it please let me know.'''


from weather_app import WeatherApp

# 1. Building a Modular Online Bookstore System
# Objective: The objective of this assignment is to create a modular online bookstore system using Python. The focus will be on applying the principle of modularity to enhance code organization, maintainability, and scalability. The system will be broken down into different modules, each handling specific functionalities of the bookstore.

# Task 1: Designing the Book Module

# Create a module for managing book-related functionalities. This includes classes and functions for book attributes, book availability, and any other book-specific operations.

# Problem Statement:

# The bookstore system requires a dedicated module for handling various aspects related to books, such as title, author, price, and stock status.

# Code Example:

# book.py

# class Book:
#     # Define book attributes and methods
#     pass

# # Additional functions related to book management
# Expected Outcome:

# A book.py module that integrates the functionalities for a book class. It should be able to change the values of title, author, price, stock, and any other attributes you choose to define.

# 2. Refactoring a Weather Forecast Application into Classes and Modules
# Objective:
# The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more structured, object-oriented, and modular format. The focus will be on identifying parts of the script that can be encapsulated into classes and organizing these classes into appropriate modules to enhance code readability, maintainability, and scalability.

# Task 1: Identifying and Creating Classes

# Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

# Problem Statement:

# The existing script for the weather forecast application is written in a procedural style and lacks organization.

# Code Example:

# Before Refactoring:

# # Weather Forecast Application Script

# def fetch_weather_data(city):
#     # Simulated function to fetch weather data for a given city
#     print(f"Fetching weather data for {city}...")
#     # Simulated data based on city
#     weather_data = {
#         "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
#         "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
#         "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
#     }
#     return weather_data.get(city, {})

# def parse_weather_data(data):
#     # Function to parse weather data
#     if not data:
#         return "Weather data not available"
#     city = data["city"]
#     temperature = data["temperature"]
#     condition = data["condition"]
#     humidity = data["humidity"]
#     return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

# def get_detailed_forecast(city):
#     # Function to provide a detailed weather forecast for a city
#     data = fetch_weather_data(city)
#     return parse_weather_data(data)

# def display_weather(city):
#     # Function to display the basic weather forecast for a city
#     data = fetch_weather_data(city)
#     if not data:
#         print(f"Weather data not available for {city}")
#     else:
#         weather_report = parse_weather_data(data)
#         print(weather_report)

# def main():
#     while True:
#         city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
#         if city.lower() == 'exit':
#             break
#         detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
#         if detailed == 'yes':
#             forecast = get_detailed_forecast(city)
#         else:
#             forecast = display_weather(city)
#         print(forecast)

if __name__ == "__main__":
    app = WeatherApp()
    app.main()


# Expected Outcome:

# A main.py script that demonstrates how the different modules and classes come together to form a fully functional weather forecast application. The script should exemplify the benefits of using OOP and modular programming in Python.