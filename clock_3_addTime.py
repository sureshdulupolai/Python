from datetime import datetime, timedelta

select_user = [
    {'1' : 1},
    {'2' : 2},
    {'5' : 5},
    {'10' : 10},
    {'15' : 15}
]

extra_time = timedelta(minutes=5)




# Current Time 
# ----------------------------------------------------------------
now = datetime.now()
currentHour = now.hour
currentMinute = now.minute
currentSecond = now.second


# Developer Side
# -----------------------------------------------------------------
new_time = now + extra_time
totalHour = new_time.hour
totalMinute = new_time.minute
totalSecond = new_time.second


# AM or Pm 
# ------------------------------------------------------------------
current_time = datetime.now().strftime("%p")

print(current_time)  # Output: AM or PM