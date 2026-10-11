arr = [2,5,1,6,10,7]
n = len(arr)

print("unsorted:: ",arr)
for i in range(n-1):
    swapped = False
    print("===================")
    print("before:: ",arr)

    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if not swapped:
        break   
    print("After:: ",arr)
print("Sorted:: ",arr)
