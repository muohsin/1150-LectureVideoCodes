import time



# how would we print a lin of 80 snow characters
while True: # give indentation/Tab
    for snow in range(80):
        print('❄️', end='') # end='' is an argument to function - customize behavior
        time.sleep(0.1) # can sleep for fraction of seconds

    print() # print nothing, but by default, we always get a newline (press enter/return)


# while True:
#     # end argument tells print what to do when it's done printing the text
#     # default is to press enter
#     # we can customize the end value to override the default behavior
#     print('❄️', end='')  # end='' is an argument to function - customize behavior
#     time.sleep(0.2) # can sleep for fractions of a second