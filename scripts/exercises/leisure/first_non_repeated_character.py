# # Brute Force - n²

string = "abdadcdbedadbcf"
# print(string)
arr = [string[i] for i in range(len(string))]


# booleans = [False] * len(arr)
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] == arr[j] and i != j:
#             booleans[i] = True

# for x in range(len(arr)):
#     if not booleans[x]:
#         print(arr[x])
#         break

# Hash Tables - Dictionaries - Linear time complexity

stored_indexes = {}
for i in range(len(arr)):
    if arr[i] in stored_indexes:
        local = stored_indexes[arr[i]]
        stored_indexes[arr[i]] = [local, i]
    else:
        stored_indexes[arr[i]] = [i]

for key, value in stored_indexes.items():
    if len(value) == 1:
        print(key)
        break