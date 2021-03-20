n, x, y = map(int, input().split())
left = 0
right = max(x, y) * n
while right > left + 1:
    m = (right + left) // 2
    if (m // x + m // y) < n:
        left = m
    else:
        right = m
print(right + min(x, y))
