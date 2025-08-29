# nested if blocks

x = 30
y = 40
z = 50

print('Start')

if x == 30:
    print('Yes, it is 30!')
    print('hello world 1!')

    if y == 40:
        print('Yes, it is 30!')
        print('hello world 2!')
    
    if y == 50:
        print('Yes, it is 30!')
        print('hello world 3!')
    
    print('In x')

print('End')