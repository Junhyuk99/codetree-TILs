arr = list(map(int, input().split()))
if arr[len(arr)-1]==0:
    arr.pop()
for i in range (len(arr)):
    print(arr.pop(), end=' ')