import time 

print(time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string
#                    epoch = when your computer thinks time began(reference point)

print()

print(time.ctime(100000000)) # print date 100000000 seconds after epoch time

print()

print(time.time()) # return current seconds since epoch

print()

print(time.ctime(time.time())) # print current time

print()

time_object = time.localtime()
print(time_object)

print()

local_time = time.strftime("%B %d %Y %H : %M %S" , time_object)# format specifiers used in time module
print(local_time)

print()

time_tuple = (2020 , 4 , 20 , 4 , 20 , 0 , 0 , 0 , 0)
time_str = time.asctime(time_tuple) # tuple representation of time an date
print(time_str)