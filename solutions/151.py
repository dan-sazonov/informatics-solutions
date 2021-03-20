# fixme частичное решение
n = int(input())
prime = [True] * (n + 1)
prime[0] = prime[1] = False
i = j = 0

for i in range(2, n + 1):
    if not prime[i]:
        continue
    for j in range(i * i, n + 1, i):
        prime[j] = False
numbers = [c[0] for c in enumerate(prime) if c[1]]


def main():
    for p in numbers:
        for q in numbers[::-1]:
            if p + q == n:
                print(p, q)
                return


main()
