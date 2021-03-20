n = int(input())
arr = sorted(map(int, input().split()))
ans = [arr[0]]

for i in range(1, n):
    if abs(arr[i - 1] - arr[i]) >= 107:
        continue
    ans.append(arr[i])

if n <= 2:
    print(*arr)
else:
    print(*ans)
