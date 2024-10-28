N = int(input())
num = 1
for i in range(1,N*N+1):
    print(num, end=' ')
    num+= 1
    if i%4==0:
        print()
    if num == 10:
        num = 1