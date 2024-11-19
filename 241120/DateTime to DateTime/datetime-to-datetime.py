a,b,c= map(int,input().split())

day, hour, mins =11, 11, 11
elapsed_time = 0

while True:
    if a < 11:
        print(-1)
        break
    elif a == 11 and b < 11:
        print(-1)
        break
    elif a == 11 and b == 11 and c < 11:
        print(-1)
        break
    if day == a and hour == b and mins == c:
        break

    elapsed_time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0
    if hour == 24:
        day += 1
        hour = 0
        mins = 0

print(elapsed_time)