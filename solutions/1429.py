# fixme частичное решение
l, n, m = map(int, input().split())
socks = [list(map(int, input().split())) for _ in range(n)]
cnt = [0] * (l + 1)
ans = []

for start, end in socks:
    for i in range(start, end + 1):
        cnt[i] += 1

for _ in range(m):
    ask = int(input())
    ans.append(cnt[ask])

print(*ans, sep='\n')
