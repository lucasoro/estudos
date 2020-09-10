# Project Euler - Exercise 3
#Lucas Oro

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


n = 600_851_475_143                 #Number we're going to work with
largestFactor = 2                   #Setting a ground largest factor, will be replaced during the execution
while(n > 1):                       #Iterating through the factors, trying to find the largest
    if not n % largestFactor:
        n /= largestFactor
    else:
        largestFactor += 1
print(largestFactor)
