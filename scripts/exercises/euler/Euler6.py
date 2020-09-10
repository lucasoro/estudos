# Project Euler - Exercise 6
#Lucas Oro

# The sum of the squares of the first ten natural numbers is 12 + 22 + ... + 102 = 385;
# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)2 = 552 = 3025;
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import numpy as np						#Used this library to create the second array;

def firstTenSum():
	array = []
	for i in range(1, 101):
		array.append(i ** 2)				#This appends the numbers to the list already squared;
	return sum(array)


def firstTenSquared():
	return sum(np.arange(1,101))**2				#Returns the sum of the values inside the list squared;


def main():
	return firstTenSquared() - firstTenSum()


print(main())
