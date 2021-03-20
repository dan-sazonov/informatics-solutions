# fixme частичное решение
n = int(input())

if n % 2 == 0 or n % 5 == 0:
    print('NO')
else:
    i = '1'
    while int(i) % n != 0:
        i += '1'
    print(i)
