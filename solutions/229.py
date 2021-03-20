# fixme частичное решение
n = int(input())
arr = list(map(int, input().split()))
i_max = 0

for i in range(len(arr)):
    if arr[i] > arr[i_max]:
        i_max = i

print(arr.pop(i_max), *arr)
