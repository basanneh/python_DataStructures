 
def mergeSort(nums):
    if len(nums) == 1:
        return

    mid = len(nums) //2

    left = nums[:mid]
    right = nums[mid:]
    # Recursive call on each half
    mergeSort(left)
    mergeSort(right)
    # Two iterators for traversing the two halves
    i = 0
    j = 0
    # Iterator for the main list
    k = 0

    while i <len(left) and j < len(right):
        if left[i] <right[j]:
            nums[k] = left[i]
            i +=1

        else:
            nums[k] = right[j]
            j +=1
        k +=1

    while i < len(left):
        nums[k] = left[i]
        i +=1
        k +=1

    while j < len(right):
        nums[k] = right[j]
        j +=1
        k +=1
myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)
