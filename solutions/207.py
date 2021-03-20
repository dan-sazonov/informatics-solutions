n = int(input())
a = 1
b = 1

for _ in range(n):
    a, b = b, a + b

print(b)
