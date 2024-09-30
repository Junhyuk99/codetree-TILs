n = int(input())
for i in range(1,n+2):
    for j in range(1,n-i+2):
        print("*", end='')
    for k in range(1,i):
        print(" ", end= ' ')
    for j in range(1,n-i+2):
        print("*", end='')
    print()