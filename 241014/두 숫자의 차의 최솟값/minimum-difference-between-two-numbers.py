n = int(input())
arr = list(map(int,input().split()))
diff = arr[1]-arr[0]
for i in range(1,len(arr)):
    if arr[i]-arr[i-1] < diff:
        diff = arr[i]-arr[i-1]
print(diff)