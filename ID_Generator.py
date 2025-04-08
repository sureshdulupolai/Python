import random

lstOfCompanyId = [
    'ADH', 'DR', 'BVI',
]
class IdGen():
    def idGeneratorForCompany(self, CompanyCode, Loop = 1):
        global Count
        NewCompanyCodeLstOfUser = []
        for Lp in range(Loop):
            CC = CompanyCode; RC = str(random.randint(1101, 10000)); CCRC = CC + RC
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

        return NewCompanyCodeLstOfUser

    def Counts(self, obj):
        Count = 0
        for DataInObjects in obj:
            Count += 1
        print(Count)

obj = IdGen()
id_obj = obj.idGeneratorForCompany(CompanyCode = lstOfCompanyId[0], Loop = 5)
print(id_obj)
obj.Counts(obj = id_obj)

# CodeOfCompanyPassing = lstOfCompanyId[0]
# idGeneratorForCompany(CompanyCode = CodeOfCompanyPassing, Loop = 5)

