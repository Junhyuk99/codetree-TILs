
class Bomb:
    def __init__(self, code, col, sec):
        self.code = code
        self.col = col
        self.sec = sec
    
a,b,c = tuple(input().split())
out = Bomb(a,b,c)
print(f"code : {out.code}")
print(f"color : {out.col}")
print(f"second : {out.sec}")