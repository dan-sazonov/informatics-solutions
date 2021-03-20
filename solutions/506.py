k, n = map(int, input().split())
a = n // k
ans2 = n % k
ans1 = a if n % k == 0 else a + 1
print(ans1, ans2 if ans2 else k)
