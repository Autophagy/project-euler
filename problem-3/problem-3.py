#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def largestPrime(num):
    x = 2
    while (num > x):
        if(num % x == 0):
            num = num/x
            x = 2
        else:
            x += 1
    return x

number = 600851475143
result = largestPrime(number)
print result
