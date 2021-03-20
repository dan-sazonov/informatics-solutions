s = input()
res = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        if sum([s[p - 1] != s[p] for p in range(i + 1, j + 1)]) <= 1:
            res.add(s[i:j + 1])

print(len(res))
