a,b = map(int,input().split())
arr = [0]*10
while a > 1:
    arr[a%b] += 1
    a = a//b
summ = 0
for ele in arr:
    summ += ele**2
print(summ)