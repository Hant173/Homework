import math


class Fraction(object):
    def __init__(self, nr, dr):
        if dr < 0:
            self.nr = -nr
        else:
            self.nr = nr

        self.nr = int(self.nr)
        self.dr = int(abs(dr))
        self.reduce()

    def __str__(self) -> str:
        if self.nr == 0:
            return str(self.nr)
        if self.dr == 0:
            raise ZeroDivisionError
        if self.dr == 1:
            return str(self.nr)
        return "%d/%d" % (self.nr, self.dr)

    def hcf(self):
        return math.gcd(self.nr, self.dr)

    def reduce(self):
        # ước số chung lớn nhất
        usc = self.hcf()
        self.nr = self.nr / usc
        self.dr = self.dr / usc

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        return Fraction(self.nr + other * self.dr, self.dr)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.nr * other.dr - other.nr * self.dr, self.dr * other.dr)
        return Fraction(self.nr + other * self.dr, self.dr)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.nr * other.dr, self.dr * other.nr)
        return Fraction(self.nr, other * self.dr)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.nr * other.dr, self.dr * other.nr)
        return Fraction(self.nr * other, self.dr)


if __name__ == '__main__':
    f1 = Fraction(1, 2)
    print(f1)
    f2 = Fraction(2, 6)
    print(f2)

    print(f'{f1} + {f2} = {f1 + f2}')
    print(f'{f1} - {f2} = {f1 - f2}')
