n = int(input())
for i in range(1,n+1):
    for j in range(1,n-(n-i)+1):
        print("*", end='')
    print()
    print()
for i in range(1,n+1):
    for j in range(1,n-i+1):
       print("*", end='')
    print()
    print()