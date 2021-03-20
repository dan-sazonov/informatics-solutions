from math import ceil

a = int(input())
b = int(input())
c = int(input())

first = (a // c + 1) * c
last = (b // c) * c

if first > last:
    ans = ceil((b - a) / 2)
else:
    steps = (last - first) // c
    ans = ceil((first - 1 - a) / 2) + ceil(c / 2) * steps + ceil((b - (last - 1)) / 2)

print(ans)
