a,b = map(int, input().split())
cnt = b-a+1
for i in range(1,5):
    for j in range(cnt):
        print(f"{b-j} * {i*2} = {(b-j)*(i*2)}", end='')
        if j != cnt-1:
            print(" / ", end='')
    print()