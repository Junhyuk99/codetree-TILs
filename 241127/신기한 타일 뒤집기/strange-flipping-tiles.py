n = int(input())  # 명령의 개수
now = 0  # 현재 위치
mini = 0  # 최소 위치
maxi = 0  # 최대 위치

# 명령 수행
for i in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'L':
        now -= a
        mini = min(mini, now)
    elif b == 'R':
        now += a
        maxi = max(maxi, now)

# 마지막 명령에 따른 타일 개수 계산
if b == 'R':  # 마지막 명령이 R일 때
    black = now - mini + 1
    white = maxi - now
elif b == 'L':  # 마지막 명령이 L일 때
    black = now - mini
    white = maxi - now + 1

print(white, black)  # 검은색과 흰색 타일 출력
