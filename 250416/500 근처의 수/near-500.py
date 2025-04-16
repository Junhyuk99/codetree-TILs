a = list(map(int, input().split()))
a.sort()
for i in range (len(a)):
    if a[i] > 500:
        if a[i] != 500:
            print (a[i-1], a[i])
            break
        else:
            print (a[i-1], a[i+1])
            break
