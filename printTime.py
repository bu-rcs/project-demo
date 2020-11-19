"""
A simple script to output current time

epoch time
current local time
current year
current day
"""


import time

#epoch time
seconds = time.time()
print("Seconds since epoch =", seconds)

#local time
local_time = time.ctime(seconds)
print("Local time:", local_time)


#time struct
result = time.gmtime(seconds)
print("year", result.tm_year)
print("day", result.tm_mday)
