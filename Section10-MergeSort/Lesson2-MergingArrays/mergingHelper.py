'''
My implementation is first, solution is second. Super close on implementing, just
forgot the 2 while loops at the end
'''

def mergeHelper(arr1, arr2):
    # make a new array for results
    results = []
    # make two pointers to keep track of where we are in both arrays
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        # compare the array values:
        if arr1[i] < arr1[j]:
            results.append(arr[i])
            print(results)
            i += 1
        elif arr2[j] < arr1[i]:
            results.append(arr[j])
            print(results)
            j += 1
    if arr1[-1]:
        results.append(arr1[j])
        j += 1
    else: 
        results.append(arr2[i])
        i += 1

    return results

def mergeHelperUdemySolution(arr1, arr2):
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

# print(mergeHelper([1,3,5], [2, 4, 6])) # This does not work, should have used 
# while loops for appending remaining elements in array that is not expended

print(mergeHelperUdemySolution([1,2, 3, 5], [2, 3, 4, 6, 8, 9, 15]))
