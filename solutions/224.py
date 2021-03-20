n = int(input())
arr = list(map(int, input().split()))
x = int(input())

for i in arr:
    if i == x:
        print('YES')
        break
else:
    print('NO')
