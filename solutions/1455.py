n = int(input())
p = []
ans = []
d = 2

while d * d <= n:
    while n % d == 0:
        p.append(d)
        n //= d
    d += 1
if n > 1:
    p.append(n)

i = 0
while i < len(p):
    tmp = p.count(p[i])
    if tmp != 1:
        ans.append('{0}^{1}*'.format(p[i], tmp))
    else:
        ans.append('{0}*'.format(p[i]))
    i += tmp

print(''.join(ans).rstrip('*'))
