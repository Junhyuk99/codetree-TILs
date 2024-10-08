n = int(input())
arr = list(map(int,input().split()))
arr2 = [ele**2 for ele in arr]
for ele in arr2:
    print(ele, end=' ')