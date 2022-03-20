matrix = []
for i in range(3):
    matrix.append(list(map(int, input().split())))

x0 = matrix[0][0] * matrix[1][1] * matrix[2][2]
x0 += matrix[0][1] * matrix[1][2] * matrix[2][0]
x0 += matrix[0][2] * matrix[1][0] * matrix[2][1]
x0 -= matrix[1][1] * matrix[2][0] * matrix[0][2]
x0 -= matrix[0][0] * matrix[2][1] * matrix[1][2]
x0 -= matrix[2][2] * matrix[1][0] * matrix[0][1]

x1 = (-1) * matrix[0][0] * matrix[1][1] + (-1) * matrix[0][0] * matrix[2][2] + (-1) * matrix[1][1] * matrix[2][2]
x1 -= (-1) * matrix[0][2] * matrix[2][0]
x1 -= (-1) * matrix[1][2] * matrix[2][1]
x1 -= (-1) * matrix[0][1] * matrix[1][0]

x2 = matrix[0][0] + matrix[1][1] + matrix[2][2]

x3 = '-1'

if x0 == 0:
    x0 = ''
else:
    x0 = str(x0)

if x1 < 0:
    x1 = str(x1) + 'x'
elif x1 == 0:
    x1 = ''
else:
    x1 = '+' + str(x1) + 'x'

if x2 < 0:
    x2 = '-' + str(x2) + 'xx'
elif x2 == 0:
    x2 = ''
else:
    x2 = '+' + str(x2) + 'xx'

result = '-xxx' + x2 + x1 + x0
print(result)
