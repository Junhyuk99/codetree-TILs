# 변수 선언 및 입력
m1, d1, m2, d2 = tuple(map(int, input().split()))
A = input()

def num_of_days(m, d):
    # 계산 편의를 위해 월마다 몇 일이 있는지를 적어줍니다. 
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    # 1월부터 (m - 1)월 까지는 전부 꽉 채워져 있습니다.
    for i in range(1, m):
        total_days += days[i]
    
    # m월의 경우에는 정확이 d일만 있습니다.
    total_days += d
    
    return total_days    


# 두 날짜간의 차이가 몇 일인지를 구합니다.
diff = num_of_days(m2, d2) - num_of_days(m1, d1)

# 알맞은 요일의 이름을 출력합니다.
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
diff_day = day_of_week.index(A)
print((diff-diff_day + 7)//7 )