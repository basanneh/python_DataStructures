arr =[100,65,78,33,5,1,6,87,21,20]
for i in range(len(arr)):
        for j in range(len(arr) -1 ):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]


print(arr)
