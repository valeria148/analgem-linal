n1 = int(input())
matrix = []
for i in range(n1):
    matrix.append(list(map(int, input().split())))

n = len(matrix)
inv_matrix = [[0] * len(matrix) for i in range(len(matrix))]
for i in range(n):
    inv_matrix[i][i] = 1

big_matrix = [[0] * len(matrix) * 2 for i in range(len(matrix))]

for i in range(n):
    for j in range(n):
        big_matrix[i][j] = matrix[i][j]
        big_matrix[i][j + n] = inv_matrix[i][j]


for k in range(n):
    for i in range(2 * n):
        big_matrix[k][i] = big_matrix[k][i] / matrix[k][k]
    for i in range(k + 1, n):
        K = big_matrix[i][k] / big_matrix[k][k]
        for j in range(2 * n):
            big_matrix[i][j] = big_matrix[i][j] - big_matrix[k][j] * K
    for i in range(n):
        for j in range(n):
            matrix[i][j] = big_matrix[i][j]

for k in range(n - 1, -1, -1):
    for i in range(2 * n - 1, -1, -1):
        big_matrix[k][i] = big_matrix[k][i] / matrix[k][k]
    for i in range(k - 1, -1, -1):
        K = big_matrix[i][k] / big_matrix[k][k]
        for j in range(2 * n - 1, -1, -1):
            big_matrix[i][j] = big_matrix[i][j] - big_matrix[k][j] * K

for i in range(n):
    for j in range(n):
        inv_matrix[i][j] = big_matrix[i][j + n]

for i in range(len(inv_matrix)):
    for j in range(len(inv_matrix[i])):
        print(round(inv_matrix[i][j]) , end=' ')
    print()

