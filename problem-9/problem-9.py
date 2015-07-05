#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def euclidFormula(m,n):
    a = pow(m,2) - pow(n,2)
    b = 2 * m * n
    c = pow(m,2) + pow(n,2)
    return (a,b,c)

def calcResult():
    for n in range(1,999):
        for m in range(n+1,999):
            triple = euclidFormula(m,n)
            if (triple[0] + triple[1] + triple[2] == 1000):
                return triple[0] * triple[1] * triple[2]

resultSum = calcResult()

print resultSum
