#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

num = 0;

with open('problem-13-input.txt') as file:
	for line in file:
		num += int(line)

print str(num)[:10]
