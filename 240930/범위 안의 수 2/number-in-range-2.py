cnt = 0
total = 0
for i in range(1,11):
    i = int(input())
    if 0 <= i <= 200:
        cnt += 1
        total += i
print(total, round(total/cnt,1))