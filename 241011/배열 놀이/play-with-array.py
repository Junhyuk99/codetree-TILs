n,q = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(q):
    arr2 = list(map(int,input().split()))
    if arr2[0] == 1:
        print(arr[arr2[1]-1])
    elif arr2[0] == 2:
        if arr2[1] in arr:
            print(arr.index(arr2[1])+1)
        else: print(0)
    elif arr2[0] == 3:
        for i in range(arr2[1]-1,arr2[2]):
            print(arr[i], end=' ')
        print()