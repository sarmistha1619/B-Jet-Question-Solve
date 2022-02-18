class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,newnd):
        if self.head is None:
            self.head = newnd
        else:
            lastnd = self.head
            while True:
                if lastnd.next is None:
                    break
                lastnd = lastnd.next
            lastnd.next = newnd

    def printlist(self,n1,n2,n3,n4,n5,n6):
        m1 = n1 / n2
        m2 = n3 / n4
        m3 = n5 / n6
        c = self.head
        while True:
            if c is None:
                break
            if m1 < m2 < m3:
                print(f"{n1}/{n2},{n3}/{n4},{n5}/{n6}")
            elif m1 < m3 < m2:
                print(f"{n1}/{n2},{n5}/{n6},{n3}/{n4}")
            elif m2 < m1 < m3:
                print(f"{n3}/{n4},{n1}/{n2},{n5}/{n6}")
            elif m2 < m3 < m1:
                print(f"{n3}/{n4},{n5}/{n6},{n1}/{n2}")
            elif m3 < m2 < m1:
                print(f"{n5}/{n6},{n3}/{n4},{n1}/{n2}")
            elif m3 < m1 < m2:
                print(f"{n5}/{n6},{n1}/{n2},{n3}/{n4},")
            c = c.next
n = int(input())
ll = LinkedList()
if 2<n<10:
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    n6 = int(input())

nd1 = Node(n1)
ll.insert(nd1)
nd2 = Node(n2)
ll.insert(nd2)
nd3 = Node(n3)
ll.insert(nd3)
nd4 = Node(n4)
ll.insert(nd4)
nd5 = Node(n5)
ll.insert(nd5)
nd6 = Node(n6)
ll.insert(nd6)
ll.printlist(n1,n2,n3,n4,n5,n6)