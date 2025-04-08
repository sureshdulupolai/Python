import random

lstOfCompanyId = [
    'ADH', 'DR', 'BVI',
]

def idGeneratorForCompany(CompanyCode, Loop = 1):
    NewCompanyCodeLstOfUser = []
    for Lp in range(Loop):
        CC = CompanyCode
        RC = str(random.randint(1, 2))
        CCRC = CC + RC
        if len(NewCompanyCodeLstOfUser) > 0:
            CopyDataPresent = 0
            # for loop using to check all id that created in list, where it is same or not
            for NccuData in NewCompanyCodeLstOfUser:
                NoOfCode = ''
                # for loop in a particular id that already genrated inside list
                for a1 in NccuData:
                    # check in id generator there is a number then condition will True else False
                    if a1.isdigit():
                        NoOfCode += str(a1)
                        # check if RC Present in list or not
                        if int(RC) == int(NoOfCode):
                            CopyDataPresent += 1   
                        else:
                            continue
            if CopyDataPresent == 0:
                NewCompanyCodeLstOfUser += [CCRC]
            else:
                pass
        else:
            NewCompanyCodeLstOfUser += [CCRC]

    # print(len(NewCompanyCodeLstOfUser))
    # print()
    # print(NewCompanyCodeLstOfUser)

CodeOfCompanyPassing = lstOfCompanyId[0]
idGeneratorForCompany(CompanyCode = CodeOfCompanyPassing, Loop = 5)