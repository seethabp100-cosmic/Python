arr = [5,4,2,6,3,7]
minValue = arr[0] #2
for i in range(len(arr)-1):
    if(minValue>arr[i+1]):
        minValue = arr[i+1]
print("lowest number from arr:: ",minValue)



minVal = arr[0]
for i in arr:
    if(i<minValue):
        minValue = arr[i]
print(minValue)