arr = list(map(int,input().split()))
sum=0
for i in range(len(arr)):
    if arr[i] == 0:
        sum += arr[i-1]
        sum += arr[i-2]
        sum += arr[i-3]
        break
print(sum)