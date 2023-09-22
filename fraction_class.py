'Fravtions class'
def solv(x, y):
    while x % y != 0:
        x1 = x
        y1 = y
        x = y1
        y = x1 % y1
    return y
class Fraction:
    def __init__(self, n, d):
        self.top = n
        self.bottom = d

    def __str__(self):
        return str(self.top)+"/"+str(self.bottom)

    def show(self):
        print(self.top,"/",self.bottom)

    def __add__(self, other):
        num = self.top * other.bottom + self.bottom * other.top
        den = self.bottom * other.bottom
        f = solv(num, den)
        return Fraction(num // f, den // f)

    def __eq__(self, other):
        firstnum = self.top * other.bottom
        secondnum = other.top * self.bottom

        return firstnum == secondnum




