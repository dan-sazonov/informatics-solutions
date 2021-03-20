# fixme частичное решение
n = int(input())
arr = list(map(int, input().split()))
i_max = 0

for i in arr:
    if i > i_max:
        i_max = i

print(i_max)
