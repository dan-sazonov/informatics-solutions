# fixme частичное решение
a, b, c = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = gcd(b, a % b)
    x, y = y, x - (a // b) * y
    return d, x, y


d, x0, y0 = gcd(a, b)

if c % d == 0:
    x = (c / d) * x0 + (b / d)
    y = (c / d) * y0 - (a / d)
    print(d, x, y)
else:
    print('Impossible')
