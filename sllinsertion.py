#1st program
#Inserting at the start of list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def printnodes(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next

def insertAtStart(head,ele):
    #Expectation:
    #1.Block creation for new value
    #2.Attaching link
    #3.Change the head
        newblock=Node(ele)
    if head==None:#if there is an empty linked list
        return newblock
    curr=head
    newblock.next=curr
    return newblock

l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
    head=insertAtStart(head,ele)
printnodes(head)

Output
110-->99-->88-->77-->66-->55-->44-->33-->22-->11-->

#2nd program
#Insert at tail
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printnodes(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()

def insertAtEndOfTail(head,ele):
    #Expectation:
    #1.It should create a new block with data as ele
    #2.it should add this block at the end of insertatendoftail
    #3.Finally it should return the head of linked list

    newblock=Node(ele)
    if head==None:#if there is an empty linked list
        return newblock
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newblock
    return head
l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printnodes(head)

Output
11-->22-->33-->44-->55-->66-->77-->88-->99-->110-->


#3rd program
#Inserting at a specific position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printnodes(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()

def insertAtEndOfTail(head,ele):
    #Expectation:
    #1.It should create a new block with data as ele
    #2.it should add this block at the end of insertatendoftail
    #3.Finally it should return the head of linked list

    newblock=Node(ele)
    if head==None:#if there is an empty linked list
        return newblock
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newblock
    return head

def insertatspecificposition(head,position,value):
    #1.Creating a new block
    #2.Add new value address in position-1 next field
    newblock=Node(value)
    index=1
    if position==1:
        newblock.next=head
        return newblock
    curr=head
    while index!=position-1:
        curr=curr.next
        index+=1
    newblock.next=curr.next
    curr.next=newblock
    return head

l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printnodes(head)
head=insertatspecificposition(head,2,25)
printnodes(head)
Output
11-->22-->33-->44-->55-->66-->77-->88-->99-->110-->
11-->25-->22-->33-->44-->55-->66-->77-->88-->99-->110-->
