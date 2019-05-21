# Fraction class.
# inspired by Goldwasser & Letscher: Object-oriented programming in Python.

def gcd(a,b):
    'returns the greatest common denominator of integers a and b'
    while b != 0:
        a, b = b, a % b
    return a
  
    
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            self.num = 0
            self.den = 0
        else:
            factor = gcd(abs(numerator), abs(denominator))
            if denominator < 0:
                factor = -factor  # we want the stored denominator to be positive.
            self.num = numerator // factor
            self.den = denominator // factor
            
    def __str__(self):
        if self.den == 0:
            return 'undefined'
        if self.den == 1:
            return str(self.num)
        return str(self.num) + '/' + str(self.den)


    def add(self,otherFraction):
        sumDen = self.den * otherFraction.den;
        sumNum = self.den*otherFraction.num + self.num*otherFraction.den
        result = Fraction(sumNum, sumDen)
        return result

    def __add__(self, other):
        return self.add(other)

    def __lt__(self, other):
        return self.num*other.den < self.den*other.num

    def __float__(self):
        return float(self.num)/self.den

    def __int__(self):
        return self.num//self.den

        

if __name__ == '__main__':
    a = Fraction(12,8)
    b = Fraction(4)
    c = Fraction()
    d = Fraction(3, 0)
    print a, b, c, d, a+b, a<Fraction(4,3), float(a), int(a)


