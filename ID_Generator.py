import random

lstOfCompanyId = [
    'ADH', 'DR', 'BVI',
]

def idGeneratorForCompany(CompanyCode, Loop = 1):
    NewCompanyCodeLstOfUser = []
    for Lp in range(Loop):
        CC = CompanyCode
        RC = str(random.randint(1, 10))
        CCRC = CC + RC
        if len(NewCompanyCodeLstOfUser) > 0:
            for NccuData in NewCompanyCodeLstOfUser:
                NoOfCode = ''
                for a1 in NccuData:
                    if a1.isdigit():
                        NoOfCode += str(a1)
            print(NoOfCode)

            # for NCCU in NewCompanyCodeLstOfUser:
            #     if CCRC not in NCCU:
            #         NewCompanyCodeLstOfUser += [CCRC]
            #         break
            #     else:
            #         continue
        else:
            NewCompanyCodeLstOfUser += [CCRC]
    
    # print(len(NewCompanyCodeLstOfUser))
    # print()
    # print(NewCompanyCodeLstOfUser)

CodeOfCompanyPassing = lstOfCompanyId[0]
idGeneratorForCompany(CompanyCode = CodeOfCompanyPassing, Loop = 100)