def binary(arr, targetVal):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right) // 2
        if arr[mid] == targetVal:
            return mid
        if arr[mid] < targetVal:
            left = mid+1
        if arr[mid] > targetVal:
            right = mid-1
    return -1

arr = [9, 11, 13, 15, 17, 19]
targetVal = 5
result = binary(arr, targetVal)
if(result == -1):
    print("Target not found in array")
else:
    print("Target value found at index: ", result)
        