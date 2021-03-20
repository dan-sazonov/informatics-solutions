from math import gcd

n, m = map(int, input().split())
print(gcd(n - 1, m - 1) + 1)
