#Array based impleementation
Q=[]
print(Q)
#Enqueue
Q.append(10)
Q.append(20)
Q.append(30)
Q.append(40)
Q.append(-50)
print(Q)
deleteelement=Q.pop(0)
print("Deleted element :",deleteelement)
print(Q)
deleteelement=Q.pop(0)
print("Deleted element :",deleteelement)
print(Q)
deleteelement=Q.pop(0)
print("Deleted element :",deleteelement)
print(Q)
deleteelement=Q.pop(0)
print("Deleted element :",deleteelement)
print(Q)
deleteelement=Q.pop(0)
print("Deleted element :",deleteelement)
print(Q)

Output
[]
[10, 20, 30, 40, -50]
Deleted element : 10
[20, 30, 40, -50]
Deleted element : 20
[30, 40, -50]
Deleted element : 30
[40, -50]
Deleted element : 40
[-50]
Deleted element : -50
[]

Q=[]
print(Q)
#Enqueue
def enqueue(Q,ele):
    Q.append(ele)
    print(ele,"is inserted in queue")
def printQ(Q):
    if len(Q)==0:
        print("Queue is empty")
        return
    print(Q)
def dequeue(Q):
    if len(Q)==0:
        print("Queue is empty")
        return 
    ele=Q.pop(0)
    print("Deleted element is",ele)
enqueue(Q,10)
enqueue(Q,20)
enqueue(Q,30)
enqueue(Q,40)
enqueue(Q,50)
printQ(Q)
dequeue(Q)
printQ(Q)
dequeue(Q)
printQ(Q)
dequeue(Q)
printQ(Q)
dequeue(Q)
printQ(Q)
dequeue(Q)
printQ(Q)

Output
[]
10 is inserted in queue
20 is inserted in queue
30 is inserted in queue
40 is inserted in queue
50 is inserted in queue
[10, 20, 30, 40, 50]
Deleted element is 10
[20, 30, 40, 50]
Deleted element is 20
[30, 40, 50]
Deleted element is 30
[40, 50]
Deleted element is 40
[50]
Deleted element is 50
Queue is empty


