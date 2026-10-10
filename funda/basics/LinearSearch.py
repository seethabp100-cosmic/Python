def LinearSearch(arr, targetVal):
    n = len(arr)
    for i in range(n-1):
        if arr[i] == targetVal:
            return i
    return -1


arr = [1,97,2,4,2,6]
result = LinearSearch(arr, targetVal=10)
if(result != -1):
    print("Target value found at index : ",result)
else:
    print("Target value not found")