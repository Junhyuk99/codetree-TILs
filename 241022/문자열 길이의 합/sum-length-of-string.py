n = int(input())
arr = [
    input()
    for _ in range(n)
]
cnt = 0
cnt2=0
for i in range(n):
    cnt += len(arr[i])
for i in range(n):
    if arr[i][0] == 'a':
        cnt2+=1
print (cnt,cnt2)