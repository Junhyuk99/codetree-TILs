N=int(input())
arr=list(map(int,input().split()))
a = 0
while a != 1:
    print(arr.index(max(arr))+1, end=' ')
    a = arr.index(max(arr))+1
    for _ in range(len(arr)-a+1):
        arr.pop()