n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    a_old = a.copy()
    tmp = a[i]
    j = i - 1
    while j >= 0 and a[j] > tmp:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = tmp
    if a != a_old:
        print(a)
