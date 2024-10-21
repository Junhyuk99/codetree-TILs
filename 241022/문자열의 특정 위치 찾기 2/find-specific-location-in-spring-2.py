arr=["apple","banana","grape","blueberry","orange"]
a = input()
cnt = 0
for i in range(len(arr)):
    if arr[i][3] == a or arr[i][2]==a:
        print(arr[i])
        cnt += 1
print(cnt)