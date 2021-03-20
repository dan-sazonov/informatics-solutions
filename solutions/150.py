# fixme частичное решение

from math import ceil

n = int(input())
cube = ceil(n ** (1 / 3)) + 1
x = y = 0

for i in range(1, cube):
    for j in range(1, cube):
        if i ** 3 + j ** 3 == n:
            x = i
            y = j
            print(x, y)
            break
    if x and y:
        break
else:
    print('impossible')
