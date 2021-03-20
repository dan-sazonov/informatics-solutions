n = int(input())
arr = list(map(int, input().split()))
m, k = map(int, input().split())

arr.insert(k - 1, m)
print(*arr)
