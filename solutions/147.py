m = int(input())
n = int(input())


def gcd(a, b):
    if b == 0 :
        return a
    return gcd(b, a % b)


print(gcd(n, m))
