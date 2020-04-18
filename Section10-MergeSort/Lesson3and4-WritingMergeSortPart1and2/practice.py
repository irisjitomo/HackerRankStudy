def mergeHelper(arr1,arr2):
    results = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            results.append(arr1[i])
            results.append(arr2[j])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            results.append(arr1[i])
            i += 1
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

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    return mergeHelper(left, right)

print(mergeSort([12,234,124124,345,3451,456456,234324]))