#DELETE TAIL NODE
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertAtEndOfTail(head,ele):
    newblock=Node(ele)
    if head==None:#if there is an empty linked list
        return newblock
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newblock
    return head
def printnodes(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def deletetailnode(head):
    curr=head
    previous=None
    while curr.next!=None:
        previous=curr
        curr=curr.next
    previous.next=None
    return head 
l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printnodes(head)
head=deletetailnode(head)
printnodes(head)

Output
11-->22-->33-->44-->55-->66-->77-->88-->99-->110-->
11-->22-->33-->44-->55-->66-->77-->88-->99-->


#2nd program
#Delete head node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertAtEndOfTail(head,ele):
    newblock=Node(ele)
    if head==None:
        return newblock
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newblock
    return head
def printnodes(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def deleteheadnode(head):
    if head==None:
         return None
    curr=head
    head=head.next
    curr.next=None
    return head
l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printnodes(head)
head=deleteheadnode(head)
printnodes(head)
head=deleteheadnode(head)
printnodes(head)

Output
11-->22-->33-->44-->55-->66-->77-->88-->99-->110-->
22-->33-->44-->55-->66-->77-->88-->99-->110-->
33-->44-->55-->66-->77-->88-->99-->110-->


#3rd program
#Delete at specific position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertAtEndOfTail(head,ele):
    newblock=Node(ele)
    if head==None:
        return newblock
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newblock
    return head
def printnodes(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def deleteheadnode(head):
    if head==None:
         return None
    curr=head
    head=head.next
    curr.next=None
    return head

def deleteSpecificNode(head,position):
    if position==1:
        return deleteheadnode(head)
    cur=head 
    index=1
    while index!=position-1:
        cur=cur.next
        index+=1
    #cur-->points to position-1
    mainnode=cur.next
    #mainnode--> points to actual position
    nextnode=mainnode.next
    #nextnode-->points to position+1
    mainnode.next=None
    cur.next=None
    cur.next=nextnode
    return head
l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printnodes(head)
head=deleteSpecificNode(head,3)
printnodes(head)
head=deleteSpecificNode(head,4)
printnodes(head)

Output
11-->22-->33-->44-->55-->66-->77-->88-->99-->110-->
11-->22-->44-->55-->66-->77-->88-->99-->110-->
11-->22-->44-->66-->77-->88-->99-->110-->
