_ = int(input())
bridges = map(int, input().split())

for n, h in enumerate(bridges):
    if h <= 437:
        print(f'Crash {n + 1}')
        break
else:
    print('No crash')
