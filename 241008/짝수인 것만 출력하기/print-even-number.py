n = int(input())
arr=list(map(int,input().split()))
arr2=[ele for ele in arr if ele%2==0]
for ele in arr2:
    print(ele, end=' ')