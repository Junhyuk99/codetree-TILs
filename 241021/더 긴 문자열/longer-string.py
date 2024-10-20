a,b = input().split()
if (len(a)>len(b)):
    print(a, len(a))
elif (len(b)>len(a)):
    print(b, len(b))
elif(len(a)==len(b)):
    print("same")