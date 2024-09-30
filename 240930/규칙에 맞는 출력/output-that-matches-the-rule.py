n = int(input())
for i in range(n):
    for j in range(n-(n-i)+1):
        print(n-i+j, end=' ')
    print()