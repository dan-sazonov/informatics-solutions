n = int(input())
arr = list(map(int, input().split()))
first = max(arr)
second = 0

for i in arr:
    if i > second and i != first:
        second = i

print(second)
