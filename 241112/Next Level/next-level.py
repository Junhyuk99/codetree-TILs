# 클래스 선언
class aa:
    def __init__(self, ids, lv):
        self.ids = ids
        self.lv = lv


# 변수 선언 및 입력
a = aa("codetree", 10)
b,c = tuple(input().split())
s = aa(b,c)
# 출력
print(f"user {a.ids} lv {a.lv}")
print(f"user {s.ids} lv {s.lv}")