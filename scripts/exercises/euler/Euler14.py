# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

# Solution 1 - Iterating through every possibility
# import time

# start = time.time()
# values = [2, 2]

# for i in range(1, 1000000):
#     local = i
#     counter = 0
#     while local > 1:
#         counter += 1
#         if not local % 2:
#             local = local / 2
#         else:
#             local = local * 3 + 1
#     if counter > values[0]:
#         values[0] = counter
#         values[1] = i


# print(values[1], time.time() - start)   # ~55 sec

# --------------------------//--------------------------//--------------------------

# Solution 2 - Memoization (poorly written)
import time

start = time.time()
stored_results = {}

for i in range(1_000_000):
    local = i
    summ = 0
    while local > 1:
        if local in stored_results:
            summ += stored_results[local]
            break
        else:
            if not local % 2:
                local /= 2
                summ += 1
            else:
                local = local * 3 + 1
                summ += 1
    stored_results[i] = summ

last_key = list(stored_results.keys())[list(stored_results.values()).index(sorted(stored_results.values())[-1])]

print("Solution: %i; time: {:.3f} seconds.".format(time.time() - start) %last_key) # ~ 4.8 sec