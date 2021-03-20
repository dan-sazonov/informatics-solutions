from collections import Counter

n, m = map(int, input().split())
letters = Counter(''.join([input() for _ in range(n)]))
words = Counter(''.join([input() for _ in range(m)]))

for letter, amount in (letters - words).items():
    print(letter * amount, sep='', end='')
print('\n')
