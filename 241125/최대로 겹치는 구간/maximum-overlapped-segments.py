n = int(input())
arr = [0 for _ in range(201)]
for _ in range(n):
    x,y = map(int,input().split())
    x += 100
    y += 100
    for i in range(x,y):
        arr[i] += 1

print(max(arr))