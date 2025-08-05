# user-defined exceptions

class InsufficientBalanceError(Exception):              # 
    def __init__(self, accountNo, currentBalance):
        self.__accno = accountNo
        self.__curbal = currentBalance
        print()

    def get_details(self):
        return {'Acc No' : self.__accno, 'Balance' : self.__curbal}

class Customers():
    def __init__(self):
        self.__dct = {}

    def append(self, accountNo, nm, bal):
        self.__dct[accountNo] = {'Name ': nm, 'Balance': bal}

    def deposit(self, accountNo, amt):
        d = self.__dct[accountNo]
        d['Balance'] = d['Balance'] + amt
        self.__dct[accountNo] = d

    def display(self):
        for k,v in self.__dct.items():
            print(k, v)
        print()

    def withdraw(self, accountNo, amt):
        d = self.__dct[accountNo]
        curbal = d['Balance']
        if curbal - amt < 5000:
            raise InsufficientBalanceError(accountNo, curbal)       # raise - creating a obj and send same data and kept in some where, it get call inside exceptions
        else:
            d['Balance'] = d['Balance'] - amt
            self.__dct[accountNo] = d

c = Customers()
print(c)


c.append(123, 'Suresh', 35000)
c.append(456, 'Kalim', 80000)
c.append(789, 'Alex', 90000)
c.append(101, 'Varsha', 40000)
c.append(112, 'Ved', 20000)
c.display()
c.deposit(789, 10000)
c.deposit(123, 20000)

try:
    c.withdraw(101, 250)
    print("amount withdrawl successfully!")
    c.display()
    c.withdraw(101, 100)
    print("amount withdrawl successfully!")
    c.display()
    c.withdraw(123, 51000)
    print("amount withdrawl successfully!")
    c.display()                                         # code execute and here only
    # c.withdraw(112, 16000)                            # not work because, for the above case the code goes in exception
    # print("amount withdrawl successfully!")
    # c.display()

except InsufficientBalanceError as ibe:
    print('Withdrawl denied!')
    print('insufficient balance!')
    print(ibe.get_details())
    print('ibe : ', ibe)
