class complex:
    count = 0

    def __init__(self, r=0.0, i=0.0):
        self.real = r
        self.imag = i

        complex.count += 1

    def __eq__(self, other):                    # operator overloading
        # take both values
        # (self.real = c1) == (other.real = c2)
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False
        
c1 = complex(1.1, 0.2)
c2 = complex(1.1, 0.2)
c3 = complex(1.1, 0.2)
c4 = complex(2.1, 0.4)
c5 = complex(1.1, 0.2)

if c1 == c2 == c3 == c4 == c5:
    print("Match")
else:
    print("Not Match")