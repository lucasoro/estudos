def squarer(list1):
    squares = list(zip(list1, list(map(lambda x: x ** 2, list1))))
    return squares


numbers = [1,2,3,4,5]
z, z = zip(*squarer(numbers))
print(z)