# fixme частичное решение
n, m = map(int, input().split())
boat = []
for _ in range(n):
    boat.extend(list(map(int, input().split())))
boat.sort()
k = int(input())
mesk = sorted(list(map(int, input().split())))
count = 0
used = []

for i in mesk:
    for j in range(len(boat)):
        if boat[j] >= i and j not in used:
            count += 1
            used.append(j)
            break

print(count)
