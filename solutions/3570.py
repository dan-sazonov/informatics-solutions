a = float(input())
right = n = int(input())
left = -1

for _ in range(200):
    m = (right + left) / 2
    if m ** n < a:
        left = m
    else:
        right = m

print(m)
