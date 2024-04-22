#First line consists a integer 'n' which denotes 'n' operations to perform. Next 'n' lines consist either of the following pattern. 
#If first element is '1' then second element would be some integer which we need to append to our existing Queue. 
#If first element is '2' we need to display front element of the Queue. 
#If first element is '3' then we need to delete and print the front element from Queue. 
#If first element is '4' then we need to print all elements present in Q with space seperated way. 
#If first element is '5' then we need to print Whether the Queue is empty or not.

n=int(input().strip()) 
class Q:
    def __init__(self,data):
        self.data=data
        self.next=None
def enqueue(head,val):
    print(val,"inserted")
    nn=Q(val)
    #nn=newnode
    if head==None:
        return nn
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=nn
    return head
def dequeue(head):
    if head==None:
        print("Queue is empty")
        return None
    sn=head.next
    print(head.data)
    #sn=secondnode
    head.next=None
    return sn
def frontvalue(head):
    if head==None:
        print("Queue is empty")
        return
    print(head.data)
def printQ(head):
    if head==None:
        print("Queue is empty")
        return 
    cur=head
    while cur!=None:
        print(cur.data,end=" ")
        cur=cur.next
    print()
head=None
while n>0:
    word = list(map(int, input().strip().split()))
    ch=word[0]
    if ch==1:
        val=word[1]
        head=enqueue(head,val)
    elif ch==2:
        frontvalue(head)
    elif ch==3:
        head=dequeue(head)
    elif ch==4:
        printQ(head)
    else:
        if head==None:
            print("Queue is empty")
        else:
            print("Queue is not empty")
    n-=1


Sample Input 0
11
1 12
1 34
1 56
1 32
2
4
3
4
5
1 222
4

Sample Output 0
12 inserted
34 inserted
56 inserted
32 inserted
12
12 34 56 32
12
34 56 32
Queue is not empty
222 inserted
34 56 32 222

