n = int(input())
ans = [0] * (n + 1)
exp = []
current = n

for i in range(2, n + 1):
    ans[i] = ans[i - 1]
    if ans[i // 2] < ans[i] and i % 2 == 0:
        ans[i] = ans[i // 2]
    if ans[i // 3] < ans[i] and i % 3 == 0:
        ans[i] = ans[i // 3]
    ans[i] += 1

while current > 1:
    if ans[current - 1] + 1 == ans[current]:
        prev = current - 1
    elif ans[current // 2] + 1 == ans[current] and current % 2 == 0:
        prev = current // 2
    else:
        prev = current // 3

    if prev * 3 == current:
        exp.append('3')
    elif prev * 2 == current:
        exp.append('2')
    else:
        exp.append('1')

    current = prev

print(*exp[::-1], sep='')
