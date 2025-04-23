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

    def limit(self, n):
        return self.data[:n]  # returns first n users


# Normal User Direct print
# ---------------------------------------------------
# User = auth.userData

# User.limit(2)
# ------------------------------------------------------
User = UserWrapper(auth.userData)