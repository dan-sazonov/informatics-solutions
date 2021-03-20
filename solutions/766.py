n = int(input())
arr = list(map(int, input().split()))


def merge(a, b):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


def merge_sort(a):
    if len(a) < 2:
        return a
    else:
        k = len(a) // 2
        return merge(merge_sort(a[:k]), merge_sort(a[k:]))


print(*merge_sort(arr))
