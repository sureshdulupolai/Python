try:
    dataStop = int(input('How Many Data Need To Enter : '))
    if dataStop > 0:
        OverAllTotal = int(input('Total For a Particular Subject : '))
        print()
        totalScore = OverAllTotal * dataStop; D1 = 0; subjectList = []; markList = []
        while dataStop > D1:
            subjectName = input('Subject Name : ')
            markObtain = float(input('Mark Obtain : '))
            subjectList += [subjectName]; markList += [markObtain]
            D1 += 1
            print()
        
        totalMarkObtain = 0
        for ML in markList:
            totalMarkObtain += ML
        
        for DataInsideList in range(len(subjectList)):
            print('Subject : {} -> Mark : {}'.format(subjectList[DataInsideList], markList[DataInsideList]))

        percentage = (totalMarkObtain / totalScore) * 100
        print('Total Percentage You Got : {}%\n'.format(percentage))

    else:
        print('Thank You For Visting!')

except:
    print('Some Error Is Comming!, Try Again')

finally:
    print('\nThanks Come Again!!')