c1, c2 = map(int, input().split())
c3, c4 = map(int, input().split())


D = (c1 + c4) ** 2 - 4 * (c1 * c4 - c2 * c3)
print(D)
if D > 0:
    result = ((c1 + c4 - D ** (1 / 2)) / 2,  (c1 + c4 + D ** (1 / 2)) / 2)
elif D == 0:
    result = (c1 + c4) / 2
else:
    result = None

if result is None:
    print(None)

elif isinstance(result, tuple):

    if c1 != result[0]:
        print(str(result[0]) + " [" + str(-c2/(c1 - result[0])) + ", 1]")
    else:
        print(str(result[0]) + " [4, 0]")

    if c4 != result[1]:
        print(str(result[1]) + " [1, " + str(-c3 / (c4 - result[1])) + "]")
    else:
        print(str(result[1]) + " [0, 6]")

else:
    if c1 != result:
        print(str(result) + " [" + str(-c2 / (c1 - result)) + ", 1]")
    else:
        print(str(result) + " [4, 0]")