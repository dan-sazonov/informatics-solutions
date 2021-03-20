n = int(input())
ans = [0] * (n + 1)
ans[0] = 1
ans[1] = 1

for i in range(1, n):
    ans[i + 1] = ans[i] + ans[i - 1]

print(str(ans[-1])[-1])
