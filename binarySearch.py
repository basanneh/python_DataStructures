
arr = [1,2,3,4,6,8,9,12,15,47,54,98,99]

key =12
def binarySearch(arr,key):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high)//2
        if key == arr[mid]:
            return mid
        if key < arr[mid]:
            high = mid -1
        else:
            low = mid +1

    return -1

print(binarySearch(arr,5))
