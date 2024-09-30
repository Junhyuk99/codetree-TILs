n = int(input())
cnt = 0
for i in range(1,n+1):
    if n/i <= 1:
        cnt += 1
        print(cnt)
        break
    n = n//i
    cnt += 1