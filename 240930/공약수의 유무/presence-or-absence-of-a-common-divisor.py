a,b = map(int, input().split())
arr=[]
cnt = 0
for i in range(1, int(1920**(2/1))+1):
    if 1920%i==0:
        if 2880%i==0:
            arr.append(1920//i)
            arr.append(i)
arr.sort()
for i in range(a, b+1):
    for j in range(len(arr)):
        if i==arr[j]:
            print(1)
            cnt += 1
            break
if cnt==0:
    print(0)