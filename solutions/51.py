arr = input()
opening = []
circle_rev = {')': '(', ']': '[', '}': '{'}

for i in arr:
    if not opening and i in (')', ']', '}'):
        print('no')
        break
    elif i in ('(', '[', '{'):
        opening.append(i)
    elif opening and circle_rev[i] == opening[-1]:
        opening.pop()
    else:
        print('no')
        break
else:
    print('no' if opening else 'yes')
