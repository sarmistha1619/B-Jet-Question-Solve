def prnt(n1,n2,n3,n4,n5,n6):
    m1 = n1 / n2
    m2 = n3 / n4
    m3 = n5 / n6

    if m1<m2<m3:
        print(f"{n1}/{n2},{n3}/{n4},{n5}/{n6}")
    elif m1<m3<m2:
        print(f"{n1}/{n2},{n5}/{n6},{n3}/{n4}")
    elif m2<m1<m3:
        print(f"{n3}/{n4},{n1}/{n2},{n5}/{n6}")
    elif m2<m3<m1:
        print(f"{n3}/{n4},{n5}/{n6},{n1}/{n2}")
    elif m3<m2<m1:
        print(f"{n5}/{n6},{n3}/{n4},{n1}/{n2}")
    elif m3<m1<m2:
        print(f"{n5}/{n6},{n1}/{n2},{n3}/{n4},")

n = int(input())
if 2<n<10:
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    n6 = int(input())

prnt(n1,n2,n3,n4,n5,n6)

