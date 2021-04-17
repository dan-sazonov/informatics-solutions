n = int(input())
k = int(input())
ans = 0

while n > 0:
    n -= k
    k += 1
    ans += 1

print(ans)
