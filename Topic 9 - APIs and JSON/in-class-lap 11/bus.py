import requests

# before pprint it was horizontal
# but when we added pprint it become vertical
from pprint import pprint

def main():
    # urls can be saved as strings in a program
    south_url = 'https://svc.metrotransit.org/NexTrip/17928?format=json'
    north_url = 'https://svc.metrotransit.org/NexTrip/17939?format=json'


    bus_tracker(north_url)



def bus_tracker(url):

    # expect to get data in JSON form
    # JSON can be converted nearly into python dictionaries and list
    response = requests.get(url).json()
    #pprint(response)  # a dictionary

    #print(type(response)) # <class 'dict'>
    #print(response.keys()) # only works for dictionaries, dict_keys(['stops', 'alerts'])

    departures_list = response['departures'] # get the value for the 'departure' key
    #pprint(departures_list) # this is a list ( of dictionaries )
    #pprint(type(departures_list)) # <class 'list'

    print('Route         Time                Description')
    print('=' * 60) # =============================================

    for bus_departure in departures_list:
        #pprint(type(bus_departure))
        #print()

        route_name = bus_departure['route_short_name']
        #print(route_name)

        departure_time = bus_departure['departure_text']
        #print(departure_time)

        description = bus_departure['description']
        description = description.strip() # removes tab characters and any other whitespaces before and after text
        #print(description)

        #print(route_name + ' ' + departure_time + ' ' + description)
        #print as a table
        print(f'{route_name:<12}  {departure_time:<15}  {description:<60}')


main()