# countdown timer

# print 10,9,8,7......1 with one second betwwn each other

import time

# variation on range - tell it where to start,
# where to stop, and how to change second variable
# each iteration
for second in range(10, 0, -1):
    print(second)
    time.sleep(1)  # sleep for 1 second

print('Starting the game!!!')