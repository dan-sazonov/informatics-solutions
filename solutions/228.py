# fixme частичное решение
n = int(input())
arr = list(map(int, input().split()))
ans = 0

for i in range(n):
    if arr[ans] > arr[i]:
        ans = i

print(ans + 1)
