from numero_e11 import matrix

matrix = matrix.strip().split("\n")
for i in range(len(matrix)):
    matrix[i] = matrix[i].split(" ")

INITIAL_ARRAY_LENGTH = len(matrix)  # 20x20 > 20
SUB_MATRICES = 4
VARIABLE_USED_IN_FOR_LOOPS = INITIAL_ARRAY_LENGTH - SUB_MATRICES + 1 # 20 + 4 - 1, sums up to 16 indexes (0 - 15)
final_result = 0

for line in range(INITIAL_ARRAY_LENGTH):
    for column in range(INITIAL_ARRAY_LENGTH):
        matrix[line][column] = int(matrix[line][column])

# Linear

for j in range(INITIAL_ARRAY_LENGTH):
    for k in range(VARIABLE_USED_IN_FOR_LOOPS):
        mult = matrix[j][k:k + 4]
        local = 1
        for item in mult:
            local *= item
            if local > final_result:
                final_result = local

# Columns

for a in range(VARIABLE_USED_IN_FOR_LOOPS):
    for b in range(INITIAL_ARRAY_LENGTH):
        local_matrix = []
        for c in range(4):
            local_matrix.append(matrix[a + c][b])
        if local_matrix[0] * local_matrix[1] * local_matrix[2] * local_matrix[3] > final_result:
            final_result = local_matrix[0] * local_matrix[1] * local_matrix[2] * local_matrix[3]

# Diagonal Multiplications - from left to right

for x in range(VARIABLE_USED_IN_FOR_LOOPS):
    if matrix[x][x] * matrix[x + 1][x + 1] * matrix[x + 2][x + 2] * matrix[x + 3][x + 3] > final_result:
        final_result = matrix[x][x] * matrix[x + 1][x + 1] * matrix[x + 2][x + 2] * matrix[x + 3][x + 3]

print(final_result)     # linear results, column results and diagonal results from left to right

# Diagonal Multiplications - from left to right