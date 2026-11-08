# Import requests so Python can get information from a website.
import requests

# This is the API link that provides the weather forecast.
# It gives us forecast information for a specific location.
url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast'

# Ask the website for weather information.
# .json() converts the information into a Python dictionary.
response = requests.get(url).json()

# Print the full response if we want to see all the information.
# print(response)

# Get the properties section from the response dictionary.
properties = response['properties']

# Get the list of forecast periods from the properties.
forecast_periods = properties['periods']

# Print the column headings for our weather report.
print('Day                 Temperature (F)    Forecast')

# Go through each forecast period one at a time.
for period in forecast_periods:

    # Get the name of the day or time period.
    name = period['name']
    # Get the temperature for that period.
    temp = period['temperature']
    # Get the weather description.
    forecast = period['detailedForecast']
    # Display the day, temperature, and forecast in organized columns.
    print(f'{name:<17}, {temp:<17}, {forecast}')
