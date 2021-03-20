import math

n = int(input())

for i in range(math.ceil(n / 2), n):
    b = i
    a = n - b
    if math.gcd(a, b) == 1:
        break

print(a, b)
