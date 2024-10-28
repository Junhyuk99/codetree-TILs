A = input()
B = input()
check = 0
for i in range(len(A)):
    A = A[-1] + A[:-1]
    if A == B:
        print(i+1)
        check = 1
        break
if check == 0:
    print(-1)