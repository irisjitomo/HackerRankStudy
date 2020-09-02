def search(arr, val):
    arr.sort()
    left = 0
    right = len(arr) - 1
    if val == arr[left]:
        return left
    elif val == arr[right]:
        return right
    while left <= right:
        middle = (left + right) // 2
        currentElement = arr[middle]
        if currentElement < val:
            left = middle + 1

        elif currentElement > val:
            right = middle - 1
        else:
            return middle

    return -1


print(search([1, 2, 3, 4, 5, 6, 12, 13, 18, 25, 34, 56, 67, 78, 99], 78))
