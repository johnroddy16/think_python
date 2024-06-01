# write a script that reads the current time and converts it to a time of day in hrs, mins, seconds and displays the # of days since 
# the epoch:

import time

print(time.time())

sec_in_day = 24 * 60 * 60
print(sec_in_day)

days_since_epoch = int(time.time() / 86400)
print(days_since_epoch)

