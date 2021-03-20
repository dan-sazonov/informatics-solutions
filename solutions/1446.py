number = int(input())
members = [[*map(int, input().split())] for _ in range(number)]
n = len(members)
unordered = True

while unordered:
    unordered = False

    for i in range(n-1):
        if members[i][1] < members[i+1][1]:
            members[i], members[i+1] = members[i+1], members[i]
            unordered = True

        elif members[i][1] == members[i + 1][1]:
            if members[i][0] > members[i + 1][0]:
                members[i], members[i + 1] = members[i + 1], members[i]
                unordered = True

    n -= 1

for j in members:
    print(*j)

