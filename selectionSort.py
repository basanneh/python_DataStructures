        
arr = [23,86,1,8,76,3,2]
print("Input Array :",arr)

for i in range(len(arr)):
            minimum = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j
            if minimum != i:
                arr[i], arr[minimum] = arr[minimum], arr[i]

print ("sorted Array")
print(arr)



