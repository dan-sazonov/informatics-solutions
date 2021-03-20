n, k, x, y = map(int, input().split())
d = (n * y) - (n // k) * (y - x)  # квартир на одном этаже
input()
ask = list(map(int, input().split()))


def find_level(f):
    """
    возвращает относительный номер этажа
    """
    level = 0
    i = 0
    while i < f:
        if (level + 1) % k == 0 and (level + 1) >= k:
            i += x
        else:
            i += y
        level += 1
    return level


def find_entry(f):
    """
    возвращает относительный номер подъезда с нуля
    """
    if f % d == 0:
        return f // d - 1
    else:
        return f // d


for flat in ask:
    if flat > d:
        print(find_level(flat - (d * find_entry(flat))))
    else:
        print(find_level(flat))
