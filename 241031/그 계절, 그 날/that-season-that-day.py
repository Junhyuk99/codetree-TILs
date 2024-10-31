Y,M,D = map(int,input().split())
def weather(y,m,d):
    if y%4==0 and y%100==0 and y%400==0:
        if m == 2:
            if d > 28:
                return(-1)
        if m==12 or m==1 or m==2:
            return("Winter")
        elif 3<=m<=5:
            return("Spring")
        elif 6<=m<=8:
            return("Summer")
        elif 9<=m<=11:
            return("Fall")

    elif y%4==0 and y%100==0:
        if m == 2:
            if d > 28:
                return(-1)
        if m==12 or m==1 or m==2:
            return("Winter")
        elif 3<=m<=5:
            return("Spring")
        elif 6<=m<=8:
            return("Summer")
        elif 9<=m<=11:
            return("Fall")

    elif y % 4==0:
        if m ==2:
            if d > 29:
                return(-1)
        if m==12 or m==1 or m==2:
            return("Winter")
        elif 3<=m<=5:
            return("Spring")
        elif 6<=m<=8:
            return("Summer")
        elif 9<=m<=11:
            return("Fall")

    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m==10 or m==12:
        if d>31:
            return(-1)
        if m==12 or m==1 or m==2:
            return("Winter")
        elif 3<=m<=5:
            return("Spring")
        elif 6<=m<=8:
            return("Summer")
        elif 9<=m<=11:
            return("Fall")

    elif m==4 or m==6 or m==9 or m==11:
        if d>30:
            return(-1)
        if m==12 or m==1 or m==2:
            return("Winter")
        elif 3<=m<=5:
            return("Spring")
        elif 6<=m<=8:
            return("Summer")
        elif 9<=m<=11:
            return("Fall")


print(weather(Y,M,D))