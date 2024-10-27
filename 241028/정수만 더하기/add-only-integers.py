a = input()
cnt = 0
for ele in a:
    if ele >= '0' and ele <= '9':
        cnt += int(ele)
print(cnt)