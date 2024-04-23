n=int(input())
l=list(map(int,input().split()))
def bs(l):
    #bs=BubbleSort
    for i in range(0,len(l)-1):
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l
            
print("Unsorted list:",l)
print("Sorted list",bs(l))

Input
6
5 3 7 6 8 2
Output
Unsorted list: [5, 3, 7, 6, 8, 2]
Sorted list [2, 3, 5, 6, 7, 8]


#Different way for implementing bubble sort
num=[22,2,36,5,28,9]
n=len(num)
def BubbleSort(num):
    for i in range(n-1,0,-1):
        for j in range(n-1):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
        print(num)
    return num

print("Before Sorting :",num)
print("After sorting : ",BubbleSort(num))

Output
Before Sorting : [22, 2, 36, 5, 28, 9]
[2, 22, 5, 28, 9, 36]
[2, 5, 22, 9, 28, 36]
[2, 5, 9, 22, 28, 36]
[2, 5, 9, 22, 28, 36]
[2, 5, 9, 22, 28, 36]
After sorting :  [2, 5, 9, 22, 28, 36]
