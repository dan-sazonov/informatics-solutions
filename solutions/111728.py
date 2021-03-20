import bisect

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ask = list(map(int, input().split()))

for i in ask:
    lb = bisect.bisect_left(arr, i)
    ub = bisect.bisect_right(arr, i)
    if lb == ub:
        print(0)
    else:
        print(lb + 1, ub)
