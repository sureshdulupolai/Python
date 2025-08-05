# type of arguments

# positional arguments
# variable - length positional arguments
# keyword arguments
# variable - length keyword arguments

# Positional Argu
def func(i, j, k):
    print(i+j)
    print(k.upper())

func(10, 20, 'python')

# Keyword arguments
def func_one(i, j, k):
    print(i, j, k)

func_one(i = 10, j = 20, k = 'cython')
func_one(j = 30, i = 100, k = 'jython')
func_one(10, k = "rython", j = 50.90)

#positional argument follows keyword argument
# func_one(k = "rython", j = 50.90, 10)
# func_one(i = 10, j = 50.90, 10)

# multiple value for argument 'i'
# func_one(10, i = 10, j = 'kython')       # solve 'j' = 10 => then print correctly 

def func_key_val(i = 101, j = 201, k = "sython"):
    print(i, j, k)

func_key_val()
func_key_val(j = 505)