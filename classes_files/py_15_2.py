# class arithmatic
class arithmatic():
    # first letter of fun contain only object address only -> ( self )
    def set_data(self, a, b):
        self.var_one = a
        self.var_two = b

    def addition(self):
        return self.var_one + self.var_two

    def subtraction(self):
        return self.var_one - self.var_two
    
    def multiplication(self):
        return self.var_one * self.var_two
    
    def quotient(self):
        return self.var_one // self.var_two
    
    def remainder(self):
        return self.var_one % self.var_two
    

# ----------------------------------------------------------------
# create a object first step
arithOne = arithmatic()         # not data inseted

# calling that obejct in which the function was define
# obj.functionName(argumentData)
arithOne.set_data(5, 2)
# calling that function which you need from inside that object
var_one = arithOne.addition()
print(var_one)

var_two = arithOne.multiplication()
print(var_two)

# ----------------------------------------------------------------
arithTwo = arithmatic()
arithTwo.set_data(7, 3)
var_thr = arithTwo.subtraction()
print(var_thr)


print()
# --------------------------------------
thr = arithTwo.addition()
four = arithOne.multiplication()

five = thr + four
print(five)