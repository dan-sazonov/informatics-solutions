w, h, n = map(int, input().split())
left = 0
right = max(w, h) * n

while right - left > 1:
    m = (right + left) // 2
    if (m // h) * (m // w) >= n:
        right = m
    else:
        left = m

print(right)
