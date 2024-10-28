a = input()
b = input()
arr1=list(a)
arr2=list(b)
arr11 = []
arr22=[]
for i in range(len(a)):
    if arr1[i] >= '0' and arr1[i] <= '9':
        arr11.append(arr1[i])

for i in range(len(b)):
    if arr2[i] >= '0' and arr2[i] <= '9':
        arr22.append(arr2[i])

arr11 = ''.join(arr11)
arr22 = ''.join(arr22)
print(int(arr11) + int(arr22))