

# import time

# print("Seconds:", time.time())  # # Current time in seconds

print()
from datetime import datetime


now = datetime.now()
print("Minute:", now.minute)  # Gets current minute
print("Second:", now.second)  # Gets current second

# now = datetime.now()
# print("Hour:", now.hour) 

now = datetime.now()

# Format time as a string
time_string = f"{now.hour}:{now.minute}:{now.second}"

# Parse string into datetime object
time_obj = datetime.strptime(time_string, "%H:%M:%S")

# print("Minute:", time_obj.minute)
# print("Second:", time_obj.second)
