# fixme частичное решение
from math import gcd

n = int(input())

for i in range(1, n):
    for j in range(i + 1, n + 1):
        if gcd(i, j) == 1:
            print(f'{i}/{j}')
