# автор - t.me/mollior

n, m = map(int, input().split())
maxs = []
mins = [-1001] * m
counts = [1] * m
for i in range(n):
    nums = list(map(int, input().split()))
    curr_min = min(nums)
    if i == 0:
        maxs = nums
    for j in range(m):
        if i != 0:
            if nums[j] > maxs[j]:
                maxs[j] = nums[j]
                counts[j] = 1
            elif nums[j] == maxs[j]:
                counts[j] += 1
        if nums[j] == curr_min and nums[j] > mins[j]:
            mins[j] = nums[j]
n_s = 0
for i in range(m):
    if mins[i] == maxs[i]:
        n_s += counts[i]
print(n_s)
