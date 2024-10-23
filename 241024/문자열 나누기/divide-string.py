n = int(input())
arr=input()
arr = arr.replace(' ', '')
cnt = 0
for i in range(0,len(arr)):
    print(arr[i], end='')
    cnt+=1
    if cnt==5:
        print()
        cnt=0