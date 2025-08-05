class Check():
    def __init__(self, lst = [], check = '', value = 0, ck = []):
        self.list = lst
        self.check = check
        self.value = value
        self.ck = ck

    def get(self):
        if len(self.list) > 0:
            if self.check in self.list[0]:
                lst1 = ()
                for a1 in range(len(self.list)):
                    if self.list[a1][self.check] == self.value:
                        lst1 += (self.list[a1],)
                    else:
                        continue
                if len(lst1) > 0:
                    context = {
                        'data' : lst1
                    }
                    return context['data']
                else:
                    return ('\n\n-- Inside {} Column, No value is Found For {} --\n\n'.format(self.check, self.value))
            
            else:
                return ('\n\n-- Table Column "{}", Does Not Exist in Table --\n\n'.format(self.check))

        else:
            return ('\n\n-- Table is Empty, Insert data into table first to fetch data --\n\n')
        
    def select(self):
        for a1 in self.list:
            print(a1)

    def sums(self):
        if len(self.list) > 0:
            if self.check in self.list[0]:
                sum1 = 0
                for i in self.list:
                    sum1 += i[self.check]
                return sum1
            else:
                return ('\n\n-- Table Column "{}", Does Not Exist in Table --\n\n'.format(self.check))
        else:
            return ('\n\n-- Table is Empty, Insert data into table first to fetch data --\n\n')
    
    def asc(self):
        if len(self.list) > 0:
            if self.check in self.list[0]:
                for a1 in range(len(self.list)):
                    for a2 in range(len(self.list)):
                        if self.list[a2][self.check] > self.list[a1][self.check]:
                            self.list[a2], self.list[a1] = self.list[a1], self.list[a2]
                return self.list
            else:
                return ('\n\n-- Table Column "{}", Does Not Exist in Table --\n\n'.format(self.check))
        else:
            return ('\n\n-- Table is Empty, Insert data into table first to fetch data --\n\n')

    def desc(self):
        if len(self.list) > 0:
            if self.check in self.list[0]:
                for a1 in range(len(self.list)):
                    for a2 in range(len(self.list)):
                        if self.list[a2][self.check] < self.list[a1][self.check]:
                            self.list[a2], self.list[a1] = self.list[a1], self.list[a2]
                return self.list
            else:
                return ('\n\n-- Table Column "{}", Does Not Exist in Table --\n\n'.format(self.check))
        else:
            return ('\n\n-- Table is Empty, Insert data into table first to fetch data --\n\n')
    
    def dis(self):
        if len(self.list) > 0:
            if self.check in self.list[0]:
                lst1 = []
                for a1 in self.list:
                    if a1[self.check] not in lst1:
                        a2 = a1[self.check]
                        lst1 += [a2]
                    else:
                        continue
                return lst1
            else:
                return ('\n\n-- Table Column "{}", Does Not Exist in Table --\n\n'.format(self.check))
        else:
            return ('\n\n-- Table is Empty, Insert data into table first to fetch data --\n\n')
        
    def group(self):
        if len(self.list) > 0:
            if self.check in self.list[0]:
                lst1 = []; tpl1 = (); lst2 = []
                for a1 in self.list:
                    if a1[self.check] not in lst1:
                        a2 = a1[self.check]; lst1 += [a2]
                    else:
                        continue
                for i in lst1:
                    a3 = i; a5 = 0
                    for a4 in self.list:
                        if a3 == a4[self.check]:
                            a5 += 1
                        else:
                            continue
                    tpl1 += (a5, )
                for b1 in range(len(lst1)):
                    lst2 += [(lst1[b1], tpl1[b1])]
                return lst2
            else:
                return ('\n\n-- Table Column "{}", Does Not Exist in Table --\n\n'.format(self.check))
        else:
            return ('\n\n-- Table is Empty, Insert data into table first to fetch data --\n\n')

    def add(self):
        print(self.ck)
        print()
        lst1 = []; lst2 = []
        for i in self.list:
            lst1 += [i,]

        
        for j in self.check:
            dct = {}
            for k,l in j:
                dct[k] = l
            lst2 += [dct]
        
        for a1 in lst2:
            lst1 += [a1]
        
        return lst1
    
    def remove(self):
        pass
    
    def update(self):
        pass

    def truncate(self):
        lst = []
        return lst

    def Datadelete(self):
        lst = []
        return lst

    def Tabledelete(self):
        del(self.list)
        return ('Table was deleted successfully')

    def show(self):
        print(self.list)
