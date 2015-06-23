#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

squareRange = range(1, 101)

diff = (pow(sum(squareRange),2) - sum([pow(x,2) for x in squareRange]))

print diff