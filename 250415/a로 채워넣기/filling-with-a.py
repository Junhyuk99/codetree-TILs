sen = input()
arr = []
for i in range (len(sen)):
    arr.append(sen[i])
arr[1] = 'a'
arr[len(arr)-2] = 'a'
for i in range(len(arr)):
    print(arr[i], end="")