from datetime import datetime

now = datetime.now()

# Current Hours Minute Second
# ------------------------------------------------------------------
time_string = f"{now.hour}:{now.minute}:{now.second}"
print(time_string)
print()


# Sorce Code For Developer Website
# -------------------------------------------------------------------
currentHour = datetime.now().hour
currentMinute = datetime.now().minute
currentSecond = datetime.now().second
# print(currentTime)

# Source Code For User Website
# -------------------------------------------------------------------
# userHour = int(input('Enter Your Hour : '))
# userMinute = int(input('Enter Your Minute : '))
# userSecond = int(input('Enter Your Second : '))


lstOfTIme = [(12, 20), (12, 15), (12, 5), (12, 30)]
print(lstOfTIme)


for A1 in lstOfTIme:
    print('Start')
    print()
    for A2 in range(len(A1)):
        if A1[0] == currentHour:
            print('Yes!, Hour is Match {}'. format(A1[0]))
            if A1[1] > currentMinute:
                print('Yes!, You Are Under Time, Curent Minute {} - Your Minute {}'.format(currentMinute, A1[1]))
            else:
                print('No!, You Are Not Allowed to Access, Time is over. Current Minute {} - Your Minute {}'.format(currentMinute, A1[1]))
        else:
            print('No!, You Are Not Allowed to Access, Time is over. Current Hour {} - Your Hour {}'.format(currentHour, A1[0]))
    print('End')
    print()

# Parse string into datetime object
# time_obj = datetime.strptime(time_string, "%H:%M:%S")
# print(time_obj)

