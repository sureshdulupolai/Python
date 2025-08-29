
#   M   <21     Married     Tax 10
#   M   <21     UnMarried   Tax 12

#   M   >=21    Married     Tax 11
#   M   >=21    UnMarried   Tax 13

#   F   <21     Married     Tax 8
#   F   <21     UnMarried   Tax 10

#   F   >=21    Married     Tax 9
#   F   >=21    UnMarried   Tax 11

gender = input("Enter the gender of the person as 'M' for Male and 'F' for Female: ").strip().upper()
age = int(input("Enter the age of the person in positive integer numbers: "))
marital_status = input("Enter the marital status of the person as 'Married' or 'Unmarried': ").strip().capitalize()

if gender == 'M':
    if (age > 0 and age < 21):
        if marital_status == "Married":
            print("Tax is 10%")

        elif marital_status == "Unmarried":
            print("Tax is 12%")

        else:
            print("Invalid entry for marital status!")
            print("The possible values could be 'Married' or 'Unmarried'")

    elif (age >= 21):
        if marital_status == "Married":
            print("Tax is 11%")

        elif marital_status == "Unmarried":
            print("Tax is 13%")

        else:
            print("Invalid entry for marital status!")
            print("The possible values could be 'Married' or 'Unmarried'")

    else:
        print('Invalid age!')
        print('The possible value of age should be a positive integer number!')

elif gender == 'F':
    if (age > 0 and age < 21):
        if marital_status == "Married":
            print("Tax is 8%")

        elif marital_status == "Unmarried":
            print("Tax is 10%")

        else:
            print("Invalid entry for marital status!")
            print("The possible values could be 'Married' or 'Unmarried'")

    elif (age >= 21):
        if marital_status == "Married":
            print("Tax is 9%")

        elif marital_status == "Unmarried":
            print("Tax is 11%")

        else:
            print("Invalid entry for marital status!")
            print("The possible values could be 'Married' or 'Unmarried'")

    else:
        print('Invalid age!')
        print('The possible value of age should be a positive integer number!')

else:
    print('Invalid entry for gender!')
    print("The possible values are 'M' and 'F'")
