n = int(input())
arr = list(map(int, input().split()))
first = second = 2e9 + 1

for i in arr:
    if i < first:
        first = i
for j in arr:
    if j < second and j != first:
        second = j

print(first, second)
