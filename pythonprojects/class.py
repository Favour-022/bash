class Complex:
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("%d+%dj" %(self.real, self.imag))
        

complex1 = Complex()
complex2 = Complex(2,3)

complex1.getData()
complex2.getData()
