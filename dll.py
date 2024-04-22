#DOUBLY LINKED LIST
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def PrintLeftToRight(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def PrintRightToLeft(tail):
    cur=tail
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.prev
    print()
ob1=Node(11)
ob2=Node(22)
ob3=Node(33)
ob1.next=ob2
ob2.prev=ob1
ob2.next=ob3
ob3.prev=ob2
PrintLeftToRight(ob1)
PrintRightToLeft(ob3)

Output
11-->22-->33-->
33-->22-->11-->


