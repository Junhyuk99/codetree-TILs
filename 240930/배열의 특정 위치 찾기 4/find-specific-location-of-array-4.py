arr = list(map(int, input().split()))
cnt = 0
cnt2=0
su = 0
for i in range(len(arr)):
    if arr[i]==0:
        break
    cnt += 1
for i in range(cnt):
    if arr[i]%2==0:
        cnt2 += 1
        su += arr[i]
print(f"{cnt2} {su}")