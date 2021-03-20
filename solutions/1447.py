n, *marks = map(int, input().split())
mark_min, mark_max = min(marks),  max(marks)
ans = [mark_min if i == mark_max else i for i in marks]

print(*ans)
