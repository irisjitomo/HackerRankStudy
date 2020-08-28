import numpy as np
import timeit

'''
import helper function here
'''
def mergeHelper(arr1, arr2):
    results = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            results.append(arr1[i])
            i += 1
        elif arr1[i] == arr2[j]:
            results.append(arr1[i])
            results.append(arr2[j])
            i += 1
            j += 1
        elif arr2[j] < arr1[i]:
            results.append(arr2[j])
            j += 1
    while i < len(arr1):
        results.append(arr1[i])
        i += 1
    while j < len(arr2):
        results.append(arr2[j])
        j += 1

    return results
'''
this uses the helper function
'''
def mergeSort(arr):
    print(arr)
    half = (len(arr) // 2)
    if len(arr) <= 1:
        return arr
    left = mergeSort(arr[:half]) # we call mergeSort here to keep cutting in half
    right = mergeSort(arr[half:]) # we call mergeSort here to keep cutting in half
    return mergeHelper(left, right) # we use the helper function to
    # sort the elements


# arr = np.random.normal(1,5,1000000)
arr = [12,1,3,16,57]

start = timeit.timeit()
print(mergeSort(arr))
# mergeSort(arr)
# print(arr)
end = timeit.timeit()
print('time:', end - start)
