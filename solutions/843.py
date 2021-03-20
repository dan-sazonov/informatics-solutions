n = int(input())
ans = [0] * (n + 2)
ans[0] = 1
ans[1] = 1

for i in range(1, n // 2 + 1):
    ans[2 * i] = ans[i] + ans[i - 1]
    ans[2 * i + 1] = ans[i] - ans[i - 1]

print(ans[-2])
