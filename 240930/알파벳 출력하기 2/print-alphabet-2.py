n = int(input())
alp = 65
for i in range(n):
    for k in range(i*2):
        print(" ",end= '')
    for j in range(n-i):
        if alp == 91:
            alp=65
        print(chr(alp), end=' ')
        alp += 1
    print()