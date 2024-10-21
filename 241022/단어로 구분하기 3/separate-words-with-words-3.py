# 공백 단위로 문자열을 입력받습니다.
string = input().split()

# 반대 순서로 문자열을 출력합니다.
for i in range(9, -1, -1):
	print(string[i])