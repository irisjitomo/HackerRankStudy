def binarySearch(arr, val):
    arr.sort()
    left = 0
    right = len(arr) - 1
    middle = (left + right) // 2
    while arr[middle] != val and left <= right:
        print('left:', arr[left], ' middle:', arr[middle], ' right:', arr[right])
        if val < arr[middle]:
            right = middle - 1
        else:
            left = middle + 1
        middle = (left + right) // 2
    print('left:', arr[left], ' right:', arr[right])
    if arr[middle] == val:
        return middle
    return -1
    

print(binarySearch([2,3,6,8,15,20,30,72,87,99,101,111,112,113,114,115,116,117,120,122,123,124,127,130,131,135,137,160,200,206,207,210,215,600,646,656,667,678,789,790,799], 200))
