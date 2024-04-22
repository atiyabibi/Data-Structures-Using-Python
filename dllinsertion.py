#Insert node at tail
#!st program
n=int(input())
l=list(map(int,input().split()))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def insertNodeAtTAil(head,data):
    nn=Node(data)
    if head==None:
        return nn
    cur=head
    while cur.next!=None:
        cur=cur.next
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
    cur=tail
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.prev
    print()
def findtail(head):
    cur=head
    while cur.next!=None:
        cur=cur.next
    return cur
head=None
for i in l:
    head=insertNodeAtTAil(head,i)
PrintLeftToRight(head)
val=findtail(head)
PrintRightToLeft(val)

Output
11-->22-->33-->44-->55-->66-->77-->88-->99-->110-->
110-->99-->88-->77-->66-->55-->44-->33-->22-->11-->


#2nd program
#Insert at head node
n=int(input())
l=list(map(int,input().split()))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def insertNodeAtHead(head,data):
    nn=Node(data)
    if head==None:
        return nn
    cur=head
    cur.prev=nn
    nn.next=head
    return nn
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
def findtail(head):
    cur=head
    while cur.next!=None:
        cur=cur.next
    return cur
head=None
for i in l:
    head=insertNodeAtHead(head,i)
PrintLeftToRight(head)
val=findtail(head)
PrintRightToLeft(val)

Output
110-->99-->88-->77-->66-->55-->44-->33-->22-->11-->
11-->22-->33-->44-->55-->66-->77-->88-->99-->110-->

#3rd program
#Insert at specific position
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
def insertAtSpecificPosition(head,data,position):
    nn=Node(data)
    if position==1:
        nn.next=head
        head.prev=nn
        return nn
    cur=head
    index=1
    while index!=position-1:
        cur=cur.next
        index+=1
    nextnode=cur.next
    nn.next=nextnode
    cur.next=nn
    nn.prev=cur
    nextnode.prev=nn
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
head=insertAtSpecificPosition(head,89,4)
PrintLeftToRight(head)
PrintRightToLeft(head)
head=insertAtSpecificPosition(head,0,1)
PrintLeftToRight(head)
PrintRightToLeft(head)

Output
11-->22-->33-->44-->55-->66-->77-->88-->99-->110-->
110-->99-->88-->77-->66-->55-->44-->33-->22-->11-->
11-->22-->33-->89-->44-->55-->66-->77-->88-->99-->110-->
110-->99-->88-->77-->66-->55-->44-->89-->33-->22-->11-->
0-->11-->22-->33-->89-->44-->55-->66-->77-->88-->99-->110-->
110-->99-->88-->77-->66-->55-->44-->89-->33-->22-->11-->0-->

