#Delete tail node
#1st program
n=int(input())
l=list(map(int,input().split()))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def insertNodeAtTail(head,data):
    nn=Node(data)
    if head==None:
        return nn
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=nn
    nn.prev=cur
    return head
def deleteTailNode(head):
    cur=head
    previous=None
    while cur.next!=None:
        previous=cur
        cur=cur.next
    previous.next=None
    cur.prev=None
    return head
def PrintLeftToRight(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def PrintRightToLeft(tail):
    tail=head
    while tail.next!=None:
        tail=tail.next
    cur=tail
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.prev
    print()
head=None
for i in l:
    head=insertNodeAtTail(head,i)
PrintLeftToRight(head)
PrintRightToLeft(head)
head=deleteTailNode(head)
PrintLeftToRight(head)
PrintRightToLeft(head)

Output
11-->22-->33-->44-->55-->
55-->44-->33-->22-->11-->
11-->22-->33-->44-->
44-->33-->22-->11-->


#2nd program
#Delete head node
n=int(input())
l=list(map(int,input().split()))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def insertNodeAtTail(head,data):
    nn=Node(data)
    if head==None:
        return nn
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=nn
    nn.prev=cur
    return head
def deleteHeadNode(head):
    if head==None:
        return None
    cur=head
    head=head.next
    cur.next=None
    head.prev=None
    return head
def PrintLeftToRight(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def PrintRightToLeft(tail):
    tail=head
    while tail.next!=None:
        tail=tail.next
    cur=tail
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.prev
    print()
head=None
for i in l:
    head=insertNodeAtTail(head,i)
PrintLeftToRight(head)
PrintRightToLeft(head)
head=deleteHeadNode(head)
PrintLeftToRight(head)
PrintRightToLeft(head)

Output
11-->22-->33-->44-->55-->
55-->44-->33-->22-->11-->
22-->33-->44-->55-->
55-->44-->33-->22-->

#3rd program
#Delete at specific position
n=int(input())
l=list(map(int,input().split()))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def insertNodeAtTail(head,data):
    nn=Node(data)
    if head==None:
        return nn
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=nn
    nn.prev=cur
    return head
def deleteHeadNode(head):
    if head==None:
        return None
    cur=head
    head=head.next
    cur.next=None
    head.prev=None
    return head
def deleteAtSpecificPosition(head,position):
    if position==1:
        return deleteHeadNode(head)
    index=1
    cur=head
    while index!=position-1:
        cur=cur.next
        index+=1
    #mn=mainnode points to actual position
    mn=cur.next
    #nn=nextnode points to next position  
    nn=mn.next
    mn.next=None
    mn.prev=None
    cur.next=nn
    nn.prev=cur
    return head
def PrintLeftToRight(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def PrintRightToLeft(tail):
    tail=head
    while tail.next!=None:
        tail=tail.next
    cur=tail
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.prev
    print()
head=None
for i in l:
    head=insertNodeAtTail(head,i)
PrintLeftToRight(head)
PrintRightToLeft(head)
head=deleteAtSpecificPosition(head,2)
PrintLeftToRight(head)
PrintRightToLeft(head)

Output
11-->22-->33-->44-->55-->
55-->44-->33-->22-->11-->
11-->33-->44-->55-->
55-->44-->33-->11-->
