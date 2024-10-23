# 문자열을 입력받습니다.
string = input()

# 문자열의 길이를 구합니다.
leng = len(string)
cnt1 = 0
cnt2 = 0
	
# 문자열 'ee'와 'eb'가 몇 번 나왔는지 확인합니다.
for i in range(0, leng - 1):
	if string[i] == 'e' and string[i + 1] == 'e':
		cnt1 += 1
	if string[i] == 'e' and string[i + 1] == 'b':
		cnt2 += 1

# 문자열 'ee'와 'eb'가 각각 몇 번 나왔는지 출력합니다.
print(cnt1, cnt2)