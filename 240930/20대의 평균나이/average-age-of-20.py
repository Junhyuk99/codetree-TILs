total = 0
cnt = 0
while True:
    n = int(input())
    if n >=30 or n <= 20:
        print (f"{total/cnt:.2f}")
        break
    cnt += 1
    total += n