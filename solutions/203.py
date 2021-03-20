n = int(input())
ans = [1, 1, 2]

if n < 3:
    print(ans[n])
else:
    for i in range(3, n + 1):
        ans.append(ans[i - 1] + ans[i - 2] + ans[i - 3])
    print(ans[-1])
