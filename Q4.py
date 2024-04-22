#First line consists a integer 'n' which denotes 'n' operations to perform. Next 'n' lines consist either of the following pattern. 
#If first element is '1' then second element would be some integer which we need to append to our existing Queue. 
#If first element is '2' we need to display front element of the Queue. 
#If first element is '3' then we need to delete and print the front element from Queue. 
#If first element is '4' then we need to print all elements present in Q with space seperated way. 
#If first element is '5' then we need to print Whether the Queue is empty or not.

#Code
Q=[]
n=int(input().strip())
while n>0:
    w=list(map(int,input().split()))
    ch=w[0]
    if ch==1:
        num=w[1]
        Q.append(num)
        print(num,"inserted")
    elif ch==2:
        if len(Q)==0:
            print("Queue is empty")
        else:
            print(Q[0])
    elif ch==3:
        if len(Q)==0:
            print("Queue is empty")
        else:
            print(Q[0])
            Q.pop(0)
    elif ch==4:
        if len(Q)==0:
            print("Queue is empty")
        else:
            for ele in Q:
                print(ele,end=" ")
            print()
    else:
        if len(Q)==0:
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

