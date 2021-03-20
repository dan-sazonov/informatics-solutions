# 40 баллов
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(key=lambda x: nums.count(x))
ans = [0] * n
i = 0
for i in range(0, n, 2):
    ans[i] = nums[i//2]
c = i//2
for j in range(n):
    if ans[j] == 0:
        c += 1
        ans[j] = nums[c]
for k in range(1, n):
    if ans[k - 1] == ans[k]:
        print(0)
        break
else:
    print(*ans)
