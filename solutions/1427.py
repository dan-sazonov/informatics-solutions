# fixme частичное решение
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix_t = list(zip(*matrix))
ans = 0

for i in matrix:
    min_el = [j for j in range(m) if i[j] == min(i)]
    for c in min_el:
        if max(matrix_t[c]) == i[c]:
            ans += 1

print(ans)
