a1, a2=map(int,input().split())
print(a1, a2, end=' ')
for _ in range(8):
    a1,a2 = a2,a2+2*a1
    print(a2, end=' ')