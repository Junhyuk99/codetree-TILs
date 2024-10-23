w = input()
n = int(input())
cnt = 0
for i in range(len(w),len(w)-n,-1):
    if cnt == len(w):
        break
    print(w[i-1], end='')
    cnt += 1