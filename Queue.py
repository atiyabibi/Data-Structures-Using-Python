
#Queue
#Linked list based implementation

class Queue:
    def __init__(self,data):
        self.data=data
        self.next=None
def enqueue(head,val):
    newnode=Queue(val)
    if head==None:
        return newnode
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=newnode
    return head
def dequeue(head):
    if head==None:
        print("Queue is empty")
        return None
    print("Deleting ",head.data)
    secondNode = head.next 
    head.next = None 
    return secondNode
def PrintQueue(head):
    if head==None:
        print("Queue is empty")
        return 
    cur = head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
head=None
head=enqueue(head,10)
head=enqueue(head,20)
head=enqueue(head,30)
head=enqueue(head,40)
head=enqueue(head,50)
PrintQueue(head)
head=dequeue(head)
PrintQueue(head)
head=dequeue(head)
PrintQueue(head)
head=enqueue(head,60)
PrintQueue(head)
head=dequeue(head)
PrintQueue(head)
head=dequeue(head)
PrintQueue(head)
head=dequeue(head)
PrintQueue(head)
head=dequeue(head)
PrintQueue(head)

Output
10-->20-->30-->40-->50-->
Deleting  10
20-->30-->40-->50-->
Deleting  20
30-->40-->50-->
30-->40-->50-->60-->
Deleting  30
40-->50-->60-->
Deleting  40
50-->60-->
Deleting  50
60-->
Deleting  60
Queue is empty
