companyListedName = ['ICIC Prudential Large & Mid Cap Fund', 'Axix Growth Opportunities Fund', 
'Tata Large & Mid Cap Fund', 'HDFC Flexi Cap Fund', 'Aditya Birla Sun Life Pure Value']
companyListEquity = ['Large & Mid Cap', 'Large & Mid Cap Fund', 'Large & Mid Cap Fund', 'Flexi Cap', 'Value']
companyListLast3yValue = [21.62, 15.39, 17.54, 24.73, 21.7]
companyListFundSize = ['17,694.45', '14,007.12', '8,342.43', '66,304.16', '6,377.82']
noOfMonth = 12
calculationOf3y = 21.62
calculationOf5y = 22.86
calculationOf7y = 15.61


userAge = int(input('Enter Age :'))
userYear = int(input("Enter Year Of Money Gain : "))
userMoney = int(input('Enter Earning : '))

a1 = (12 * userYear) * userMoney
a2 = userAge + userYear
print('You will get total {} at the age of {}'.format(a1, a2))


print(); print('Do You Need To Start \'SIP\' With Us')
user1 = input('Enter Yes or No : ').lower()
if 'y' in user1:
    print(); print('SIP Invest Ment Company Name and Equity Value :')
    for noOne in range(len(companyListedName)):
        print("""No : {} 
Name : {} 
Equity : {} 
Last 3Y : {}%p.a
Fund Size : {}Cr""".format(noOne + 1, companyListedName[noOne], companyListEquity[noOne], companyListLast3yValue[noOne], companyListFundSize[noOne]))
        print()
    userSipInp = int(input('Enter a No Wich You Need To Invest :'))
    if userSipInp >= 1:
        print(); print('How Much Do You Need To Invest'); userAmount = int(input('Min Value 50 : '))
        if userAmount > 49:
            print(); print('How Much Year Do You Need To Invest According To Your Salary Year Or Else ?'); userYearInp = int(input('Min Year 3Y : '))
            if userYearInp < 3:
                print('Minimum 3Y You Need To Invest Any Of The Given Fund')
            elif (userYearInp == 3 or userYearInp == 4):
                print(); print('You Need To Take Monthly Sip or One - Time Sip ?'); userInpHow = int(input('Enter 1 or 2 : '))
                if userInpHow == 1:
                    a1 = (((userYearInp * noOfMonth) * userAmount)); a2 = ((calculationOf3y * a1) / 100); print('Total Amount {} After Investment. Total Investment {}'.format(a1+a2, a1)); print('Profit {} in SIP'.format(a2)); print('{}% You Will Get'.format(calculationOf3y))
                elif userInpHow == 2:
                    a2 = (userAmount * (1 + (calculationOf3y / 100)) ** userYearInp); print('Total Amount {} After Investment. Total Investment {}'.format((round(a2, 2)), userAmount)); print('Profit {} in SIP'.format(round(round(a2, 2)) - userAmount , 2)); print('{}% You Will Get'.format(calculationOf3y))
                else:
                    print('{},This Thing Not Found In Your System, You Mean \'No\''.format(userInpHow))
            elif (userYearInp == 5 or userYearInp == 6):
                print(); print('You Need To Take Monthly Sip or One - Time Sip ?'); userInpHow = int(input('Enter 1 or 2 : '))
                if userInpHow == 1:
                    a1 = ((userYearInp * noOfMonth) * userAmount); a2 = ((calculationOf5y * a1) / 100); print('Total Amount {} After Investment. Total Investment {}'.format(a1+a2, a1)); print('Profit {} in SIP'.format(a2)); print('{}% You Will Get'.format(calculationOf5y))
                elif userInpHow == 2:
                    a2 = (userAmount * (1 + (calculationOf5y / 100)) ** userYearInp); print('Total Amount {} After Investment. Total Investment {}'.format((round(a2, 2)), userAmount)); print('Profit {} in SIP'.format(round(round(a2, 2)) - userAmount , 2)); print('{}% You Will Get'.format(calculationOf5y))
                else:
                    print('{},This Thing Not Found In Your System, You Mean \'No\''.format(userInpHow))
            elif userYearInp >= 7:
                print(); print('You Need To Take Monthly Sip or One - Time Sip ?'); userInpHow = int(input('Enter 1 or 2 : '))
                if userInpHow == 1:
                    a1 = ((userYearInp * noOfMonth) * userAmount); a2 = ((calculationOf7y * a1) / 100); print('Total Amount {} After Investment. Total Investment {}'.format(a1+a2, a1)); print('Profit {} in SIP'.format(a2)); print('{}% You Will Get'.format(calculationOf7y))
                elif userInpHow == 2:
                    a2 = (userAmount * (1 + (calculationOf7y / 100)) ** userYearInp); print('Total Amount {} After Investment. Total Investment {}'.format((round(a2, 2)), userAmount)); print('Profit {} in SIP'.format(round(round(a2, 2)) - userAmount , 2)); print('{}% You Will Get'.format(calculationOf7y))  
                else:
                    print('{},This Thing Not Found In Your System, You Mean \'No\''.format(userInpHow))
            else:
                print('This {}Yr Not Vaild To Invest In SIP'.format(userYearInp))
        else:
            print('This {} amount Is Not Valid To Invest In SIP'.format(userAmount))
    else:
        print('{} Is Not Valid Number To Take SIP Of Any Company'.format(userSipInp))
elif 'n' in user1:
    print('Ok Thank You For Connecting Us')
else:
    print('Choose Option Was Not Match With Out data Base Because Of That We Mean As \'No\'')