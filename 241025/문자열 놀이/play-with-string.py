s,q = input().split()
q = int(q)
new = list(s)
for _ in range(q):
    arr = list(input().split())
    if arr[0] == '1':
        c = new[int(arr[1])-1]
        new[int(arr[1])-1] = new[int(arr[2])-1]
        new[int(arr[2])-1] = c
        for ele in new:
            print(ele, end='')
        print()
    elif arr[0] == '2':
        for i in range(len(new)):
            if new[i] == arr[1]:
                new[i] = arr[2]
        for ele in new:
            print(ele, end='')
        print()