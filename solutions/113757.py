a = int(input())
b = int(input())
c = int(input())
x = 0

while (2 * a + 3 * b + 4 * c + 5 * x) / (a + b + c + x) < 3.5:
    x += 1

print(x)
