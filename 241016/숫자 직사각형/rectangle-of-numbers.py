a,b = map(int,input().split())
num = 1
arr=[
    [0 for _ in range(b)]
    for _ in range(a)      
]
for i in range(a):
    for j in range(b):
        arr[i][j] = num
        num += 1
for row in arr:
    for ele in row:
        print(ele, end=" ")
    print()