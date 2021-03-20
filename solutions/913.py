n = int(input())
a = 1
b = 2
for _ in range(1, n):
    a, b = b, a + b

print(b)
