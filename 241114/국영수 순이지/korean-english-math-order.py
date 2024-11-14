n = int(input())
class Stu:
    def __init__(self,name,kor,eng,mat):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat

students=[]
for _ in range(n):
    name,kor,eng,mat = tuple(input().split())
    students.append(Stu(name,int(kor),int(eng),int(mat)))

students.sort(key=lambda x:(-x.kor, -x.eng, -x.mat))
for i in range(n):
    print(f"{students[i].name} {students[i].kor} {students[i].eng} {students[i].mat}")