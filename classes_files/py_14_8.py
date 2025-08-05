# local variable cannot change with access variable
# to  change local variable value you need to redeclare the variable
def func():
    a = 10
    b = 20
    c = 30

    print(locals())

    locals()['a'] = 25  # not changing value
    locals()['b'] = 50
    locals()['c'] = 75

    print(locals())

    # change with this function only after go in print(a, b, c), the it will change here value again which you set first time

    var1 = locals()
    print(locals())

    var1['a'] = 600
    print(var1)

    a = 900
    
    # after this is become by default value (a as 10)
    print(a, b, c)


func()