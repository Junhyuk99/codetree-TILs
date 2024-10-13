n = int(input())
arr = list(map(int, input().split()))
print(min(arr), end=' ')
print(arr.count(min(arr)))