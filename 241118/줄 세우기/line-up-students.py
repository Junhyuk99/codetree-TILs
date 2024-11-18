n = int(input())
class Stu:
    def __init__(self,hei,wei,num):
        self.hei=hei
        self.wei=wei
        self.num=num

students=[]
for i in range(1,n+1):
    hei,wei = tuple(input().split())
    students.append(Stu(int(hei),int(wei),int(i)))

# for rank, num in enumerate(nums, start=1):
#     num_to_rank[num] = rank

students.sort(key=lambda x:(-x.hei, -x.wei, x.num))
for i in range(n):
    print(f"{students[i].hei} {students[i].wei} {students[i].num}")