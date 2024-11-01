N = int(input())
arr = list(map(int,input().split()))
def abss(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    for ele in arr:
        print(ele, end=' ')

abss(arr)