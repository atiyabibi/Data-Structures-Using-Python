#Array implementation of stack

def push(stack, val):
    stack.insert(0, val)
    print(val, "inserted")
 
def pop(stack):
    if len(stack) == 0:
        print("Stack is empty, can't delete anything")
        return 
    print(stack[0], "deleted")
    stack.pop(0)
 
def printStack(stack):
    if len(stack) == 0:
        print("Stack is empty, nothing to print")
        return 
    print(stack)
 
stack = []
push(stack, 10)
push(stack, 20)
push(stack, 30)
push(stack, 40)
push(stack, 50)
push(stack, 60)
printStack(stack)

pop(stack)
printStack(stack)

pop(stack)
printStack(stack)

pop(stack)
printStack(stack)
 
pop(stack)
printStack(stack)
 
pop(stack)
printStack(stack)

pop(stack)
printStack(stack)
 
pop(stack)
printStack(stack)

Output
10 inserted
20 inserted
30 inserted
40 inserted
50 inserted
60 inserted
[60, 50, 40, 30, 20, 10]
60 deleted
[50, 40, 30, 20, 10]
50 deleted
[40, 30, 20, 10]
40 deleted
[30, 20, 10]
30 deleted
[20, 10]
20 deleted
[10]
10 deleted
Stack is empty, nothing to print
Stack is empty, can't delete anything
Stack is empty, nothing to print

 
