# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a² + b² = c²,
# For example, 3² + 4² = 9 + 16 = 25 = 5².
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time

def discoverTriplets():
    m = [i for i in range(200, 1000)]
    for a in m:
        for b in m:
            for c in m:
                if a == b or b == c or c == a:
                    continue
                if a < b < c:
                    if (((a ** 2) + (b ** 2)) == (c ** 2)):
                        if ((a + b + c) % 1000 == 0):
                            elapsed = time.time() - start
                            print("Time: {:.5f} seconds".format(elapsed))
                            return a * b * c


start = time.time()
print(discoverTriplets())
