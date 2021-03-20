n = int(input())
ans = [0] * (n + 1)

for i in range(2, n + 1):
    ans[i] = ans[i - 1]
    if ans[i // 2] < ans[i] and i % 2 == 0:
        ans[i] = ans[i // 2]
    if ans[i // 3] < ans[i] and i % 3 == 0:
        ans[i] = ans[i // 3]
    ans[i] += 1

print(ans[-1])
