s = str(input())

n = len(s)
s1 = s[:-(n // 2)] + s[:n // 2][::-1]

if s == '9':
    print('11')
    exit()

if s1 > s:
    print(s1)
    exit()

n1 = (n + 1) // 2
n2 = n - n1
N = str(int(s[:n1]) + 1)
S2 = N + N[:n2][::-1]
print(S2)
