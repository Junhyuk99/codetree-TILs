n = int(input())
cnt = n//4
cnt -= n//100
cnt += n//400
print(cnt)