from math import ceil

n = int(input())
k = int(input())
a = n - k
ans = ceil(a / 2)

if ans < k:
    print(0)
else:
    print(ans - k)
