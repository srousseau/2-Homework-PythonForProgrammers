# Scott Rousseau
# Homework 2
# Queestion 1

# coding: utf-8
class Quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        PositiveNumber = '+'
        NegativeNumber = '-'
        if (self.a == 1):
            part1 = 'x^2'
        elif(self.a == -1):
            part1 = '-x^2'
        else:
            part1 = str(self.a) + 'x^2'
        if (self.b > 1):
            part2 = '+' + str(self.b) + 'x'
        elif (self.b == 1):
            part2 = '+x'
        else:
            part2 = str(self.b) + 'x'
        if (self.c >= 0):
            part3 = '+' + str(self.c)
        else:
            part3 = str(self.c)
        QuadraticExpression = part1 + part2 + part3
        return QuadraticExpression
    def __add__(self,other):
        return Quadratic(self.a + other.a, self.b + other.b, self.c + other.c)
    def __sub__(self,other):
        return Quadratic(self.a - other.a, self.b - other.b, self.c - other.c)
    def __eq__(self, other):
        if(self.a == other.a and self.b == other.b and self.c == other.c):
            return True
        else:
            return False

if __name__ == "__main__":
    Q1 = Quadratic(3, 8, -5)
    print Q1
    Q2 = Quadratic(2, 3, 7)
    print Q2
    quadsum = Q1 + Q2
    print "The sum is", quadsum
    quaddiff = Q1 - Q2
    print "The difference is", quaddiff
