#First line consists a integer 'n' which denotes 'n' operations to perform. Next 'n' lines consist either of the following pattern. 
#If first element is '1' then second element would be some integer which we need to append to our existing Queue. 
#If first element is '2' we need to display front element of the Queue. 
#If first element is '3' then we need to delete and print the front element from Queue. 
#If first element is '4' then we need to print all elements present in Q with space seperated way. 
#If first element is '5' then we need to print Whether the Queue is empty or not.

S=[]
n=int(input().strip())
while n>0:
    w=list(map(int,input().split()))
    ch=w[0]
    if ch==1:
        num=w[1]
        S.insert(0,num)
        print(num,"inserted")
    elif ch==2:
        if len(S)==0:
            print("Stack is empty")
        else:
            print(S[0])
    elif ch==3:
        if len(S)==0:
            print("Stack is empty")
        else:
            print(S[0])
            S.pop(0)
    elif ch==4:
        if len(S)==0:
            print("Stack is empty")
        else:
            for ele in S:
                print(ele,end=" ")
            print()
    else:
        if len(S)==0:
            print("Stack is empty")
        else:
            print("Stack is not empty")
    n-=1

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
