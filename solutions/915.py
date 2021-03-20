n = int(input())
price = list(map(int, input().split()))
a = b = 0

for i in range(n):
    a, b, = b, min(a, b) + price[i]

print(b)
