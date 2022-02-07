all_e = [
    ("0","1"),("0","2"),("1","2"),("1","3"),("2","4"),("3","4",),("4","5"),("5","6")]
class Graph:
    def __init__(self,N):
        self.n=N
        self.a_l={}

        for i in self.n:
            self.a_l[i] = []

    def a_e(self, u,v):
            self.a_l[u].append(v)
            self.a_l[v].append(u)

    def p_a_l(self):
            for i in self.n:
                d = self.a_l[i]
                print("\n", i, end="")
                for j in d:
                    print("-->",j, end="")

n = ["0","1","2","3","4","5","6"]
graph = Graph(n)

for u,v in all_e:
    graph.a_e(u,v)
print("Output: Adjacency List: ")
graph.p_a_l()
s=0
l=[]
print("\nOutput: Adjacent Matrix:")
for i in range(len(n)):
    print("\n")
    for j in range(len(n)):
        if (i==0 and j==1) or  (j==0 and i==1):
            s=s+6
            print(6,end='  ')
        elif (i==0 and j==2) or  (j==0 and i==2):
            s=s+7
            print(7,end='  ')
        elif (i==1 and j==2) or  (j==1 and i==2):
            s=s+13
            print(13,end='  ')
        elif(j==1 and i==3):
            s=s+8
            print(8,end='  ')
        elif (i == 2 and j==4) or (j == 2 and i == 4):
            s=s+10
            print(10, end='  ')
        elif (i==3 and j==4) or  (j==3 and i==4):
            s=s+9
            print(9,end='  ')
        elif (i==4 and j==5) or  (j==4 and i==5):
            s=s+11
            print(11,end='  ')
        elif (i==5 and j==6) or  (j==5 and i==6):
            s=s+12
            print(12,end='  ')
        else:
            print(0,end='  ')

print("\nOutput: Total Summation=",s)