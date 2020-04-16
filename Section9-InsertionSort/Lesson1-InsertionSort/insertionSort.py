'''
# Insertion sort pseuodocode
- Start by picking the second element in the array
- Now compare the second element with the one before it and swap if necessary
- Continue to the next element and if it is in the incorrect order,
    iterate through the sorted portion(i,e, the left side) to place the 
    element in the correct place.
'''

def insertionSort(arr):
    for i in range(1, len(arr)):
        print(arr)
        currentVal = arr[i]
        print('currentVal ', currentVal)
        j = i - 1
        print('j ', arr[j])
        while j >= 0 and currentVal < arr[j]:
            arr[j+1] = arr[j]
            print('arr[j+1] ', arr[j+1])
            j -= 1
            print('new j: ', arr[j])
        print('currentVal is less than arr[j]')
        print('swapping: ', arr[j+1], ' with currentVal: ', currentVal)
        arr[j+1] = currentVal
        print('swapped: ', arr[j+1])
    return arr


print(insertionSort([5,3,4,1,2]))