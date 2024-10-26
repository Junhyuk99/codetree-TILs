A = input()
o = input()
o = list(o)
for i in range(len(o)):
    if o[i] == 'L':
        A = A[1:] + A[0]
    elif o[i] == 'R':
        A = A[-1] + A[:-1]
print(A)