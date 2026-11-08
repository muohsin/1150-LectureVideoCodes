# Import requests so Python can get information from a website.
import requests

# This URL connects to the exchange rate API.
# It asks for the exchange rate from US dollars to Euros.
url = 'https://1150-exchange-rates.azurewebsites.net/latest'
# ?base=USD&symbols=EUR
# Query parameters
query_parameters = {'base': 'USD', 'symbol': 'EUR'}


# Send a request to the website and get the information.
# .json() changes the website's response into a Python dictionary.
response = requests.get(url, params=query_parameters).json()
# Display the full information we received from the API.
print(response)

# Get the exchange rates from the dictionary.
rates = response['rates']
# Display the exchange rates.
print(rates)

# Get the exchange rate for Euros.
euro_exchange_rate = rates['EUR']
# Display the exchange rate.
print(euro_exchange_rate)

# Ask the user how many US dollars they want to convert.
# float() allows the user to enter decimal numbers too.
dollars = float(input('Enter number of dollars: '))

# Multiply the dollars by the exchange rate to get Euros.
euros = dollars * euro_exchange_rate
# Display the final amount in Euros.
print(f'${dollars:.2f} is equivalent to {euros:.2f} Euros')
