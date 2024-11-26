n = int(input())
white = 0
black = 0
now = 0
mini = 0
maxi = 0
for i in range(n):
    a,b = input().split()
    a = int(a)
    if b == 'L':
        now -= a
        if now <= mini:
            mini = now
    elif b == 'R':
        now += a
        if now >= maxi:
            maxi = now
    if i == n-1:
        if b == 'L':
            white = maxi-now
            black = now-mini
        elif b == 'R':
            white = maxi-now
            black = now-mini
print(white,black)