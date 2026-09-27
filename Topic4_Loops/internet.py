from urllib import request # used to connect to internet resource
from time import sleep # sleep will pause the program for a time
import os

# a url for a website that we expect to be available, if we are online
url ='https://www.google.com'
second_to_sleep_between_checks = 3


while True:
    print('checking if online....')
    try:
        # open the url. this will error/fail if you are not online
        request.urlopen(url).read()
        print('You are probably online!')
        # shout out to the user1 this only works on Macs.
        os.system('say hey user, you are online')

    except:
        print('You are not online')

    print(f'Sleeping for {second_to_sleep_between_checks} seconds')
    print()
    sleep(second_to_sleep_between_checks)
