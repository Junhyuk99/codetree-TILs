cnt = 0
arr = []
while True:
    a = input()
    if a == '0':
        break
    cnt += 1
    if cnt%2 != 0:
        arr.append(a)
print(cnt)
for ele in arr:
    print(ele)