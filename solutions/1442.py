# fixme частичное решение
x = int(input())
c = []
i = 0

while len(c) <= x:
    if i * i not in c:
        c.append(i * i)
    if i ** 3 not in c:
        c.append(i ** 3)

    i += 1

print(c[x])
