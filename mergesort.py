 
def mergeSort(nums):
    if len(nums) == 1:
        return

    mid = len(nums) //2

    left_half = nums[:mid]
    right_half = nums[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i <len(left_half) and j < len(right_half):


def merge(low,mid,high):
