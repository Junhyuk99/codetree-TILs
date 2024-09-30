n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            print("*",end='')
        print(' ',end='')
    print()
    n -= 1