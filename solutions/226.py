n = int(input())
arr = list(map(int, input().split()))
x = int(input())
ans = []

for i in range(n):
    if arr[i] == x:
        ans.append(i + 1)

print(*sorted(ans))
