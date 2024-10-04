arr = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(len(arr)):
    if i%2==0:
        sum1 += arr[i]
    elif i%2==1:
        sum2 += arr[i]
print(abs(sum1-sum2))