print("Input:")
ll=[]
l2=[]
for j in range(3):
    for i in range(2):
        l = list(map(str, input().split()))

    def sq(x):
        return (int(l[0])/int((l[1])))

    m=list(map(sq, l))
    l2=l2+m
l2.sort()
print(l2)