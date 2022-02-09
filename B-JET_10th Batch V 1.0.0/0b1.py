print("Input:")
a=int(input("a="))
r=int(input("r="))
p=int(input("p="))
n=int(input("n="))
sum=0
for i in range(1, n+1):
    sum=sum + (a+(i*r))**p

print("result = ",sum+a)