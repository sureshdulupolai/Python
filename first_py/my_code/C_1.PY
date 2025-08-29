# Program To Caluclate a Percentage Of Rupess With Year.
# Sip - One-Time Investment
# Percantage Of Year Wise
# 0Y -3Y = 22.80%
# 4Y- 5Y = 24.09%
# 6Y - MORE THEN 7Y = 16.95%

investingAmount = int(input("Enter a Investing Value : "))
yearOfInvestment = int(input("Enter a Year Of Investment (3, 5, 7)Y : "))
choiceOfProcess = input("Enter You Need 'SIP Or One-Time' : ").lower()
if 'sip' in choiceOfProcess:
    if yearOfInvestment <= 3:
        percentageOfInvestment = 22.80
        calculationOfAmount = (investingAmount * 12 * yearOfInvestment)
        totalOfReturn = (calculationOfAmount + ((percentageOfInvestment / 100) * calculationOfAmount))
        print("Investment Of #{} Could have Been:".format(calculationOfAmount))
        print("Return #{} : ({}+)".format(round(totalOfReturn, 2),percentageOfInvestment))
    elif yearOfInvestment <= 5:
        percentageOfInvestment = 24.09
        calculationOfAmount = (investingAmount * 12 * yearOfInvestment)
        totalOfReturn = (calculationOfAmount + ((percentageOfInvestment / 100) * calculationOfAmount))
        print("Investment Of #{} Could have Been:".format(calculationOfAmount))
        print("Return #{} : ({}+)".format(round(totalOfReturn, 2),percentageOfInvestment))
    elif yearOfInvestment >= 6:
        percentageOfInvestment = 16.80
        calculationOfAmount = (investingAmount * 12 * yearOfInvestment)
        totalOfReturn = (calculationOfAmount + ((percentageOfInvestment / 100) * calculationOfAmount))
        print("Investment Of #{} Could have Been:".format(calculationOfAmount))
        print("Return #{} : ({}+)".format(round(totalOfReturn, 2),percentageOfInvestment))
    else:
        print("Enter Valid Investment Year To Calculate the investment")
elif 'one' in choiceOfProcess:
    if yearOfInvestment <= 3:
        percentageOfInvestment = 22.80
        calculationOfAmount = (investingAmount * yearOfInvestment)
        totalOfReturn = (calculationOfAmount + ((percentageOfInvestment / 100) * calculationOfAmount))
        print("Investment Of #{} Could have Been:".format(calculationOfAmount))
        print("Return #{} : ({}+)".format(round(totalOfReturn, 2),percentageOfInvestment))
    elif yearOfInvestment <= 5:
        percentageOfInvestment = 24.09
        calculationOfAmount = (investingAmount * yearOfInvestment)
        totalOfReturn = (calculationOfAmount + ((percentageOfInvestment / 100) * calculationOfAmount))
        print("Investment Of #{} Could have Been:".format(calculationOfAmount))
        print("Return #{} : ({}+)".format(round(totalOfReturn, 2),percentageOfInvestment))
    elif yearOfInvestment >= 6:
        percentageOfInvestment = 16.80
        calculationOfAmount = (investingAmount * yearOfInvestment)
        totalOfReturn = (calculationOfAmount + ((percentageOfInvestment / 100) * calculationOfAmount))
        print("Investment Of #{} Could have Been:".format(calculationOfAmount))
        print("Return #{} : ({}+)".format(round(totalOfReturn, 2),percentageOfInvestment))
    else:
        print("Enter Valid Investment Year To Calculate the investment")
else:
    print("Enter a Valid Investment Process Sip or One-Time")