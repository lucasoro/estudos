# Project Euler - Exercise 5
#Lucas Oro

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def euler5(num):
	result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 			# List generated in order to break the while loop;
	count = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]		# List wich contains the numbers targeted in the module operation;

	while True:												
		for i in range(10):
			if (num % count[i] == 0):
				result[i] = num				# Replaces numbers that meet the requirements in the result array;
			else:
				num += 2520				# Increments the number by the factor of 2520 (Smallest number divisible by 1 - 10;
		if all(x == result[0] for x in result):			# Checks if all values stored within the result array are equal;
			return result[0]
		
		
print(euler5(2520))
