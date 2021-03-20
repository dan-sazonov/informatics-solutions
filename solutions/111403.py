# fixme частичное решение
c = int(input())
left = 0
right = c

for _ in range(200):
    m = (right + left) / 2
    if m * m + (m ** 0.5) >= c:
        right = m
    else:
        left = m

print(right)
