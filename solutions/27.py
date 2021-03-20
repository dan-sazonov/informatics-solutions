a, b = map(int, input().split())
g = abs(a)
y = b
while y > 0:
    g, y = y, g % y

c = a // g
d = b // g

print(c, d)
