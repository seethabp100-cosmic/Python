unsortedArray = [7,12,9,11,3]
arraySize  = len(unsortedArray)
for i in range(1,arraySize):  #  1,5
    insertIndex = i  #1
    current_val = unsortedArray[i]  #12
    for j in range(insertIndex-1,-1,-1):
        if unsortedArray[j]>current_val:
            unsortedArray[j+1] = unsortedArray[j]
            insertIndex = j
        else:
            break
    unsortedArray[insertIndex] = current_val
print("Insert Sort:: ",unsortedArray)