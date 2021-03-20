from math import gcd
a, b, c, d = map(int, input().split())

m = a * d + c * b
n = d * b
div = gcd(m, n)

print(m // div, n // div)