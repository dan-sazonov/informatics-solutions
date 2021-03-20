n = int(input())
arr = list(map(int, input().split()))
x = int(input())
counter = 0

for i in arr:
    if i == x:
        counter += 1

print(counter)
