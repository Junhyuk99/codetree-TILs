n = int(input())
n = n*2
for i in range(1,n//2+1):
    for j in range(1,i*2):
        print("*", end= '')
    print()