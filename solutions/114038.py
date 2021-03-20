l = int(input())
r = int(input())
a = int(input())
counter = 0

for i in range(l, r + 1):
    counter += (r - i) // a

print(counter)