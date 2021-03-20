from math import gcd

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    g = arr[0]
else:
    g = gcd(arr[0], arr[1])
    for i in arr[2:]:
        g = gcd(g, i)
        if g == 1:
            break
print(g)
