n1,n2 = map(int,input().split())    
A = list(map(int,input().split()))
B = list(map(int,input().split()))
c = 0
for i in range(n1-n2):
    cnt = 0
    for j in range(n2):
        if B[j] != A[i+j]:
            break
        cnt += 1
    if cnt == n2:
        print("Yes")
        c = 1
        break
    
if c == 0:
    print("No")