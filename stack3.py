#First line consists a integer 'n' which denotes 'n' operations to perform. Next 'n' lines consist either of the following pattern. 
#If first element is '1' then second element would be some integer which we need to append to our existing Queue. 
#If first element is '2' we need to display front element of the Queue. 
#If first element is '3' then we need to delete and print the front element from Queue. 
#If first element is '4' then we need to print all elements present in Q with space seperated way. 
#If first element is '5' then we need to print Whether the Queue is empty or not.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
def push(top, val):
    print(val, "inserted")
    newNode = Node(val)
    newNode.next = top
    return newNode
def topValue(top):
    if top == None:
        print("Stack is empty")
        return
    print(top.data)

def pop(top):
    if top == None:
        print("Stack is empty")
        return None
    print(top.data)
    temp = top.next
    top.next = None
    return temp

def printStack(top):
    if top == None:
        print("Stack is empty")
        return
    curr = top
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next
    print()

def printStackEmpty(top):
    if top == None:
        print("Stack is empty")
    else:
        print("Stack is not empty")
top = None
n = int(input().strip())
while n > 0:
    word = list(map(int, input().split()))
    ch = word[0]
    if ch == 1:
        num = word[1]
        top = push(top, num)
    elif ch == 2:
        topValue(top)
    elif ch == 3:
        top = pop(top)
    elif ch == 4:
        printStack(top)
    else:
        printStackEmpty(top)
    n -= 1

Input 1
7
1 10
1 20
2
4
3
5
4

Output 1
10 inserted
20 inserted
20
20 10
20
Stack is not empty
10
