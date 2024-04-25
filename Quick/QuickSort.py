l=[10,5,100,50,25,80,110,108]
n=len(l)
print("Before Sorting",l)

def findPivotIndex(l,left,right):
    #Storing pivot
    pivot=l[right]
    #3Steps
    #1.Moving pivot to its actual position
    #2.Moving all smaller elements to left of pivot
    #3.Moving all greater elements to the right of pivot

    position=left
    for i in range(left,right):
        if l[i] < pivot:
            temp=l[position]
            l[position]=l[i]
            l[i]=temp
            position+=1
    temp=l[right]
    l[right]=l[position]
    l[position]=temp
    return position

def QuickSort(l,left,right):
    #Whenever there are single length arrays,there is no need to find pivot 
    if left>=right:
        return
    pivotIndex=findPivotIndex(l,left,right)
    print(l)
    QuickSort(l,left,pivotIndex-1)
    QuickSort(l,pivotIndex+1,right)
QuickSort(l,0,n-1)
print("After sorting:",l)

Output
Before Sorting [10, 5, 100, 50, 25, 80, 110, 108]
[10, 5, 100, 50, 25, 80, 108, 110]
[10, 5, 50, 25, 80, 100, 108, 110]
[10, 5, 25, 50, 80, 100, 108, 110]
[5, 10, 25, 50, 80, 100, 108, 110]
After sorting: [5, 10, 25, 50, 80, 100, 108, 110]

#if l=[10,9,7,4,5,6,3,2,1]
Before Sorting [10, 9, 8, 7, 4, 5, 6, 3, 2, 1]
[1, 9, 8, 7, 4, 5, 6, 3, 2, 10]
[1, 9, 8, 7, 4, 5, 6, 3, 2, 10]
[1, 2, 8, 7, 4, 5, 6, 3, 9, 10]
[1, 2, 8, 7, 4, 5, 6, 3, 9, 10]
[1, 2, 3, 7, 4, 5, 6, 8, 9, 10]
[1, 2, 3, 7, 4, 5, 6, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
After sorting: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
