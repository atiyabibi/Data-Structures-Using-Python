def mergeTwoArrays(left, mid, right, nums):
    index1 = left
    index2 = mid + 1 
    temp = []
    while index1 <= mid and index2 <= right:
        if nums[index1] > nums[index2]:
            temp.append(nums[index2])
            index2 += 1 
        else:
            temp.append(nums[index1])
            index1 += 1 
#If index of one array is finished the below code just add the remaining element of that array to the sorted list
    while index1 <= mid:
        temp.append(nums[index1])
        index1 += 1 
    while index2 <= right:
        temp.append(nums[index2])
        index2 += 1 
 #Maps the elements to its correct position in the list
    curr = 0
    for position in range(left, right + 1):
        nums[position] = temp[curr]
        curr += 1 
 
def divideIt(left, right, nums):
    #print(left, "-", right)
    if left >= right:
        return
    mid = (left + right) // 2
    divideIt(left, mid, nums)
    divideIt(mid + 1, right, nums)
    mergeTwoArrays(left, mid, right, nums)
 
nums = [12, 10, 3, 34, 11, 40, 24]
print("Before", nums)
divideIt(0, len(nums) - 1, nums)
print("After", nums)

Output
Before [12, 10, 3, 34, 11, 40, 24]
After [3, 10, 11, 12, 24, 34, 40]
