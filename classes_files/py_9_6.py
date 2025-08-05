engineers = {'Varsha', 'Mansi', 'Gurshish', 'Suresh', 'Kajal', 'Kalim', 'Meetali', 'Alex'}
managers = {'Vedh', 'Archie', 'Hanosh', 'Piyush', 'Hemant', 'Kalim', 'Alex'}
ceo = {'Alex'}

# union - all people in all 3 categories
print(engineers | managers | ceo)

# intersection

# who are enginers and managers
print(engineers & managers)

# who are engineers, managers, and ceo
print(engineers & managers & ceo)

# difference

# engineers who are not managers
print(engineers - managers)

# managers who are not engineers
print(managers - engineers)


# symmetric difference 
# who are engineers and not managers 
# and who are managers and not engineers
print(engineers ^ managers)

