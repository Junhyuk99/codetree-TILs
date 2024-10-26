w,q = input().split()
q = int(q)
for _ in range(q):
    a = int(input())
    if a == 1:
        w = w[1:] + w[0]
        print(w)
    elif a == 2:
        w = w[-1] + w[:-1]
        print(w)
    elif a == 3:
        w  = w[::-1]
        print(w)