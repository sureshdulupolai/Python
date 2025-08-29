class auth:
    userData = [
        {"username": "suresh","first_name": "Suresh","last_name": "Polai","gmail": "suresh@gmail.com","password": "Krish123",},
        {"username": "arjun_raj","first_name": None,"last_name": None,"gmail": "arjun.raj@gmail.com","password": "Arjun@2023",},
        {"username": "neha_singh","first_name": "Neha","last_name": None,"gmail": "neha.singh@gmail.com","password": "Neha#123",},
        {"username": "rahulmehta","first_name": None,"last_name": "Mehta","gmail": "rahul.mehta@gmail.com","password": "Mehta@456",},
        {"username": "priyapatel","first_name": None,"last_name": None,"gmail": "priya.patel@gmail.com","password": "Patel789",},
        {"username": "vikas_sharma","first_name": "Vikas","last_name": "Sharma","gmail": "vikas.sharma@gmail.com","password": "Vikas*321",}
    ]

class UserWrapper:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return repr(self.data)  # So print() shows clean list

    def limit(self, n):
        try:
            return UserWrapper(self.data[:n])
        except Exception as e:
            print("\n'Error Is Occuring : {}'".format(e))

    def feildValue(self, variable):
        try:
            lst = [item[variable] for item in self.data if item.get(variable) is not None]
            return UserWrapper(lst)
        except:
            return "Field is not exist : '{}'".format(variable)

    def removeFeild(self, *variable):
        try:
            cleaned_data = []
            for item in self.data:
                new_item = {k: v for k, v in item.items() if k not in variable}
                cleaned_data.append(new_item)
            return UserWrapper(cleaned_data)
        except Exception as e:
            print("\n'Error Is Occuring : {}'".format(e))
    
    def ASC(self, field = [], data = ''):
        try:

            if len(field) > 0:
                if (bool(type(field[0]) == dict) == False):
                    lstOfData = field; AdditionalList = []; StrList = []

                    for FCheck in range(len(lstOfData)):

                        if type(lstOfData[FCheck]) == str:
                            StrList += [lstOfData[FCheck]]

                        else:
                            AdditionalList += [lstOfData[FCheck]]
                    
                    for F1 in range(len(StrList)):
                        for F2 in range(len(StrList) - 1):

                            if StrList[F1][:1] < StrList[F2][:1]: 
                                StrList[F1], StrList[F2] = StrList[F2], StrList[F1]
                    
                    LastList = StrList + AdditionalList
                    return LastList

            elif len(field) == 0:
                if self.data and data:
                    print('debug 1')

            else:
                return "No Value Is Present Inside List"
            
        except Exception as e:
            print("\n'Error Is Occuring : {}'".format(e))

    def DSC(self, field = [], data = ''):
        if field:
            for F1 in range(len(field)):
                for F2 in range(len(field)):
                    if field[F1][:1] > field[F2][:1]:
                        field[F1], field[F2] = field[F2], field[F1]
            return field
                
        else:
            self.data
            pass
        
# Normal User Direct print
# ---------------------------------------------------
# User = auth.userData

# User.limit(2)
# ------------------------------------------------------
User = UserWrapper(auth.userData)