n = int(input())
arr = list(map(int,input().split()))
arr2=[]
for i in range(1,len(arr)+1):
    arr2.append(arr[i-1])
    if i%2==1:
        arr2.sort()
        print(arr2[len(arr2)//2], end=' ')