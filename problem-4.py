#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def checkIfPalindromic(num):
	#convert number into string
	string = str(num)

	#check whether the string is equal to its reversed string
	if (string == string[::-1]):
		return True
	else:
		return False

highestPalindrome = 0

for x in range(999,0,-1):
	for y in range(999,0,-1):
		if ((x*y) > highestPalindrome):
			if(checkIfPalindromic(x*y)):
				highestPalindrome = x * y

print highestPalindrome
