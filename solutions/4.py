import bisect

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ask = list(map(int, input().split()))

for i in ask:
    if bisect.bisect_left(arr, i) == bisect.bisect_right(arr, i):
        print('NO')
    else:
        print('YES')