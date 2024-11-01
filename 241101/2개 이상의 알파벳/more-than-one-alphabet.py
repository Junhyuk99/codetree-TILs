arr = list(input())
cnt = 0
for i in range(len(arr)):
    if arr[i] != arr[0]:
        cnt = 1
if cnt == 1:
    print("Yes")
else:
    print("No")