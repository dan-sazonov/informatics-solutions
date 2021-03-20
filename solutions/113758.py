from math import ceil, floor, sqrt

a = int(input())
b = int(input())
k = int(input())
ans = 0

for y in range(1, 10 ** 6 + 1):
    if a <= y ** 3 <= b:
        f = floor(sqrt(min(b, y ** 3 + k)))
        c = ceil(sqrt(max(a, y ** 3 - k)))
        ans += f - c + 1
    elif y ** 3 > b:
        break

print(ans)
