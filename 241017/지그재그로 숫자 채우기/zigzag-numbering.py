n,m = map(int,input().split())
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
num = 0
for i in range(m):
    if i%2==0:        
        for j in range(0,n,1):
            arr[j][i] = num
            num += 1
    elif i%2==1:
        for j in range(n-1,-1,-1):
            arr[j][i] = num
            num += 1
for row in arr:
    for ele in row:
        print(ele, end= ' ')
    print()