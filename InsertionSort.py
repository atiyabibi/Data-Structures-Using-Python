nums=[12,3,10,28,9,200,267]
def InsertionSort(nums):
    n=len(nums)
    for i in range(1,n):
        temp=nums[i]
        position=i-1
        while position>=0 and nums[position]>temp:
            nums[position+1]=nums[position]
            position-=1
        nums[position+1]=temp
        print(nums)
    return nums
print("Before Sorting:",nums)
print("After Sorting :",InsertionSort(nums))


Output
Before Sorting: [12, 3, 10, 28, 9, 200, 267]
[3, 12, 10, 28, 9, 200, 267]
[3, 10, 12, 28, 9, 200, 267]
[3, 10, 12, 28, 9, 200, 267]
[3, 9, 10, 12, 28, 200, 267]
[3, 9, 10, 12, 28, 200, 267]
[3, 9, 10, 12, 28, 200, 267]
After Sorting : [3, 9, 10, 12, 28, 200, 267]
