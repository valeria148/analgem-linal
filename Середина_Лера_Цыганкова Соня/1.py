n1 = int(input())
matrix1 = []
for i in range(n1):
    matrix1.append(list(map(int, input().split())))

n2 = int(input())
matrix2 = []
for i in range(n2):
    matrix2.append(list(map(int, input().split())))

flag_sum = True
if len(matrix1) == len(matrix2) and  len(matrix1[0]) == len(matrix2[0]):
    sum_matrix = [[0] * len(matrix1[0]) for i in range(len(matrix1))]
    for i in range(len(sum_matrix)):
        for j in range(len(sum_matrix[i])):
            sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
else:
    flag_sum = False
    print("Can't find sum")



flag_mult = True
if len(matrix1[0]) == len(matrix2):
    mult_matrix = [[0] * len(matrix2[0]) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                mult_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
else:
    flag_mult = False
    print("Can't find multiply")




if flag_sum:
    for i in range(len(sum_matrix)):
        for j in range(len(sum_matrix[i])):
            print(sum_matrix[i][j], end=' ')
        print()
print()
print("------------------")
print()
if flag_mult:
    for i in range(len(mult_matrix)):
        for j in range(len(mult_matrix[i])):
            print(mult_matrix[i][j], end=' ')
        print()