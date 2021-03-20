n = int(input())

while True:
    if n % 2 == 0:
        print('prime' if n == 2 else 'composite')
        break
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    print('prime' if d * d > n else 'composite')
    break
