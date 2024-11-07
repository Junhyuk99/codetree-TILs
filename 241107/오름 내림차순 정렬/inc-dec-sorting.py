n = int(input())
arr=list(map(int,input().split()))
arr.sort()
for ele in arr:
    print(ele,end=' ')
arr.sort(reverse=True)
print()
for ele in arr:
    print(ele,end=' ')