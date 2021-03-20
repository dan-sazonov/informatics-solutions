n = int(input())
k = int(input())
ans = 0

while n > 0:
    n -= k  # инвариант из условия, только в обратном порядке
    k += 1
    ans += 1  # сделали еще один шаг

print(ans)
