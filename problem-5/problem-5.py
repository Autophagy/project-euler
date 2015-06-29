#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Greatest common divisor between 2 numbers
def GCD(a,b):
	if (b == 0):
		return a
	else:
		return GCD(b, a % b)

#Lowest common multiple between 2 numbers
def LCM(a,b):
	return ((a*b) / GCD(a,b));

#Find the LCM of more than 2 numbers via recursion
#Eg. LCM(x,y,z) = LCM(x,LCM(y,z)))
def multiLCM(numbers):
	while (len(numbers) > 1):
		x = numbers.pop()
		i = len(numbers)
		numbers[i - 1] = LCM(numbers[i - 1], x)

	return numbers[0]


x = multiLCM(range(1,21))
print x
