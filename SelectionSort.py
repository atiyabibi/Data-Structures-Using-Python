num=[22,2,36,5,28,9,89,1,64]
 
def performSelectionSort(nums):
    n = len(nums)
    for fixThisIndex in range(n - 1, 0, -1):
        maxEle = nums[fixThisIndex]
        maxEleIndex = fixThisIndex 
 
        for index in range(fixThisIndex):
            if nums[index] > maxEle:
                maxEleIndex = index 
                maxEle = nums[index]
        if fixThisIndex != maxEleIndex:
            temp = nums[maxEleIndex]
            nums[maxEleIndex] = nums[fixThisIndex]
            nums[fixThisIndex] = temp
        print(nums)
    return nums
print("Before Sorting :",num)
print("After sorting : ",performSelectionSort(num))

Output
Before Sorting : [22, 2, 36, 5, 28, 9, 89, 1, 64]
[22, 2, 36, 5, 28, 9, 64, 1, 89]
[22, 2, 36, 5, 28, 9, 1, 64, 89]
[22, 2, 1, 5, 28, 9, 36, 64, 89]
[22, 2, 1, 5, 9, 28, 36, 64, 89]
[9, 2, 1, 5, 22, 28, 36, 64, 89]
[5, 2, 1, 9, 22, 28, 36, 64, 89]
[1, 2, 5, 9, 22, 28, 36, 64, 89]
[1, 2, 5, 9, 22, 28, 36, 64, 89]
After sorting :  [1, 2, 5, 9, 22, 28, 36, 64, 89]
