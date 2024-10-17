n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
num = 1
for i in range(n-1,-1,-1):
    if (n-i+1)%2==0:
        for j in range(n-1,-1,-1):
            arr[j][i] = num
            num += 1
    if (n-i+1)%2==1:
        for j in range(0,n):
            arr[j][i] = num
            num += 1

for row in arr:
    for ele in row:
        print(ele, end= ' ')
    print()