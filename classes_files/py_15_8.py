class complex:
    count = 0

    def __init__(self, r=0.0, i=0.0):
        self.real = r
        self.imag = i

        complex.count += 1
        print("This is {} run to the __init__ function".format(complex.count))

    def __add__(self, other):
        z = complex()                       # 101                       # 112
        z.real = self.real + other.real     # 101.real > 2.3            # 112.real > 3.6
        z.imag = self.real + other.imag     # 101.imag > 0.5            # 112.imag > 0.9
        return z
    
    def display(self):                       # self = 112
        print(self.real, self.imag)          # ( 112.real = 3.6 ), ( 112.imag = 0.9 )

                                        # add   > add.real  add.imag
c1 = complex(1.1, 0.2)                  # 123   >   1.1        0.2
c2 = complex(1.2, 0.3)                  # 456   >   1.2        0.3
c3 = complex(1.3, 0.4)                  # 789   >   1.3        0.4

c4 = c1 + c2 + c3
# c4 = 101 + c3     => c4 = z + c3  -- "z" variable can create multiple time, but address should be change
# c4 = 112
c4.display()        #112.display( ( 112.real = 3.6 ),( 112.imag = 0.9 ) )