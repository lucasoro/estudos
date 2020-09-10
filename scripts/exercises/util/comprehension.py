movies = ["Star Wars", "Matrix", "X-Men", "Joker", "Avengers", "Spider-Man"]

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

print([x ** 2 for x in range(1, 101)])
print([names for names in movies if names[0] == "M"])
print([(a, b) for a in A for b in B])