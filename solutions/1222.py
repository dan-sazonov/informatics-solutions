# fixme частичное решение
n = int(input())


def gcd(a, b, c, d):
    if a == c and b == d:
        return True
    while b > 0:
        a, b = b, a % b
        if a == c and b == d:
            return True
    return False


for _ in range(n):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print('YES' if gcd(a, b, c, d) else 'NO')
