# Project Euler - Exercise 4
#Lucas Oro

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# Three numbers:
def primeiros3():
  fatores = [0]
  for i in range(800, 1000):
    for j in range(800, 1000):
      vf = str(i * j)
      interior = vf[1:len(vf) - 1]
      interior2 = interior[1:len(vf) - 1]
      if ((vf[0] == vf[len(vf) - 1]) and (interior[0] == interior[len(interior) - 1]) and (interior2[0] == interior2[1]) and (int(vf) > int(fatores[0]))):
        fatores[0] = vf
        fatores.append(i)
        fatores.append(j)
  final = [int(fatores[0]), fatores[len(fatores) - 2], fatores[len(fatores) - 1]]
  return tuple(final)

  
print(primeiros3())

# Two numbers:
# def primeiros():
#   fatores = [0]
#   for i in range(40, 100):
#     for j in range(40, 100):
#       vf = str(i * j)
#       a = vf[0]
#       interior = vf[1:len(vf) - 1]
#       d = vf[3]
#       if ((a == d) and (interior[0] == interior[1]) and (int(vf) > int(fatores[0]))):
#         fatores[0] = vf
#         fatores.append(i)
#         fatores.append(j)
#   final = [int(fatores[0]), fatores[len(fatores) - 2], fatores[len(fatores) - 1]]
#   return tuple(final)


# print(primeiros())

