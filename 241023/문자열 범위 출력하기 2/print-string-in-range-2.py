w = input()
n = int(input())
for i in range(len(w),len(w)-n,-1):
    print(w[i-1], end='')