#Binary search
nums=[12,34,2,56,90,33,89,120,20]
#Function to sort a list
nums=sorted(nums)
target=89
left=0
right=len(nums)-1
found=False
#Time complexity is O(log n) i.e order of log n
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        found=True
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
if found==True:
    print("Target found")
else:
    print("Target Not Found")

Output
Target found



#Taking inputs from the user
nums=int(input())
l=list(map(int,input().split()))
#Time complexity of linear search is order of n where n is length of list
#Function to sort a list
nums=sorted(l)
target=int(input())
left=0
right=len(nums)-1
found=False
#Time complexity is O(log n) i.e order of log n
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        found=True
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
if found==True:
    print("Target found")
else:
    print("Target Not Found")

Input 1
10
36 45 2 9 10 68 45 33 99 5
45
Output 1
Target found
Input 2
10
36 45 2 9 10 68 45 33 99 5
343
Output
Target Not Found


