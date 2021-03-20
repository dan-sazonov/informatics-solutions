from math import sqrt


def is_sqrt(n):
    if n >= 0 and sqrt(n).is_integer():
        print(int(sqrt(n)))
        exit(0)


k = int(input())
x = 1
is_sqrt(k)

while k <= 10 ** 12:
    k += x
    is_sqrt(k)
    x += 2

print('none')
