a,b = input().split()
n1 = 0
n2 = 0
for i in range(len(a)):
    if a[i] < '0' or a[i] >'9':
        n1 = i
        break
for i in range(len(b)):
    if b[i] < '0' or b[i] >'9':
        n2 = i
        break
a = a[:n1]
b = b[:n2]
print(int(a)+int(b))