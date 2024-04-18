
#1st program
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
ob1=Node(20)
ob2=Node(30)
ob3=Node(40)
ob4=Node(50)
ob1.next=ob2
ob2.next=ob3
ob3.next=ob4
cur=ob1
while cur!=None:
    print(cur.data,end="-->")
    cur=cur.next

Output
20-->30-->40-->50-->

#2nd program
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
obj1=Node(11)
obj2=Node(22)
obj3=Node(33)
obj4=Node(44)
obj5=Node(55)
obj6=Node(66)
obj7=Node(77)
obj8=Node(88)
obj9=Node(99)
obj10=Node(110)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
obj9.next=obj10
cur=obj1
while cur!=None:
    print(cur.data,end="-->")
    cur=cur.next

Output
11-->22-->33-->44-->55-->66-->77-->88-->99-->110-->

#3rd program
#Without creating object for each and every data
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def printnodes(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next

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
