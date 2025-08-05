def fun_one():
    y = 20
    print(x, y)

    def fun_two():
        z = 30
        print(x, y, z)
    
    fun_two()

x = 10
fun_one()
print(x)