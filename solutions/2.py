# fixme частичное решение
import bisect

n, k = map(int, input().split())
first = sorted(map(int, input().split()))
second = list(map(int, input().split()))

for i in second:
    if bisect.bisect_left(first, i) == bisect.bisect_right(first, i):
        print(first[bisect.bisect_right(first, i) - 1])
    else:
        print(i)
