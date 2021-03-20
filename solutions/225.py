# fixme частичное решение
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
i_min = 1001

for i in arr:
    if abs(i - x) < i_min:
        ans = i
        i_min = abs(i - x)

print(ans)
