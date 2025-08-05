courses = {
    'CS101':'CPP',
    'CS102':'DS',
    'CS201':'OOP',
    'CS226':'DAA',
    'CS601':'Crypt',
    'CS442':'Web'
}

# adding a key:value pair to the existing dictionry
courses['CS444'] = 'Web Services'
print(courses)

# True = 1, False = 0
courses[True] = 'Web Ser 1'
print(courses)

courses[1] = 'Web Ser 2'
print(courses)

# updating the 'value' of the 'key:value' pair
courses['CS201'] = 'OOP Using Java'
print(courses)

# copy and paste some data in other
courses['CS102'] = courses['CS102'] + courses['CS601']
print(courses)

# 
courses[10 + 20] = 'Alpha'
print(courses, 'debug 1')

# change all value to 'alpha', right to left ( <- ). because, 30 key carring values 'alpha'
courses['CS102'] = courses['CS601'] = courses[30]
print(courses)

# deleting an item from the dictionary
# del(courses('CS102'))
# print(courses)

# clearing all the elements in a dictionary
courses.clear()
print(courses)

# deleting the entire distionary
# del(courses)
# print(courses)        # not declare