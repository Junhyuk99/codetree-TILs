class a:
    def __init__(self, code, pl, time):
        self.code = code
        self.pl = pl
        self.time = time

x = list(input().split())
a1=a(x[0],x[1],x[2])
print("secret code :",a1.code)
print("meeting point :",a1.pl)
print("time :",a1.time)