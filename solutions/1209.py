n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))
cnt = [0] * (n + 1)

for i in p:
    cnt[i] += 1
for j in range(1, n+1):
    print('yes' if cnt[j] > c[j-1] else 'no')
