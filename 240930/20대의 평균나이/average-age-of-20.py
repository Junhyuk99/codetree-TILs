total = 0
cnt = 0
while True:
    n = int(input())
    if n >=30 or n < 20:
        cal = total/cnt
        print ("%.2f" %cal)
        break
    cnt += 1
    total += n
    print(total, cnt)