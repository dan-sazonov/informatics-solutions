x = input()
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input().split())

for i in zip(*matrix):
    print('YES' if x in i else 'NO')
