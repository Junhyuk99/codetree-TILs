n,k,t = input().split()
n = int(n)
k = int(k)
arr = [0 for _ in range(n)]
for i in range (n):
    arr[i] = input()
arr.sort()
cnt = 0
for i in range(n):
    if arr[i].startswith(t):
        cnt += 1
        if cnt == k:
            print(arr[i])
            break