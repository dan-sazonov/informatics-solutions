# fixme частичное решение
from collections import Counter, deque

n = int(input())
s = Counter(input()).items()
odd = []
even = []
ans_left = deque()
ans_right = deque()

for i in s:
    if i[1] % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

for j in sorted(even):
    half = j[0] * (j[1] // 2)
    ans_right.appendleft(half)
    ans_left.append(half)

max_odd = max(odd, key=lambda x: x[1]) if odd else ('', 0)
print(*ans_left, max_odd[0] * max_odd[1], *ans_right, sep='')
