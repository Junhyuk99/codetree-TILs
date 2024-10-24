a = input()
b = input()
cnt=0
for i in range(0,len(a)-len(b)+1):
    arr=""
    for j in range(len(b)):
        arr+=a[j+i]
        if(arr==b):
            cnt+=1
        
print(cnt)