n = int(input())
arr = [0 for _ in range(n)]
for i in range(0,n):
    arr[i] = input()

arr.sort()
for ele in arr:
    print(ele)