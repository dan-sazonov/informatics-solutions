# fixme частичное решение
from math import floor, gcd

n = int(input())
g_max = ans_1 = ans_2 = 0

if n % 2 == 0:
    ans_1, ans_2 = n // 2, n // 2
else:
    first = list(range(1, floor(n / 2) + 1))
    second = list(range(n - 1, floor(n / 2), -1))
    for a, b in zip(first, second):
        if gcd(a, b) >= g_max:
            g_max = gcd(a, b)
            ans_1, ans_2 = a, b

print(ans_1, ans_2)
