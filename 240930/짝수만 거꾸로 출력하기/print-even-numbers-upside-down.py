n = int(input())
arr = list(map(int, input().split()))
arr2 = []
for ele in arr:
    if int(ele)%2==0:
        arr2.append(ele)
for ele in arr2:
    print(ele, end= ' ')