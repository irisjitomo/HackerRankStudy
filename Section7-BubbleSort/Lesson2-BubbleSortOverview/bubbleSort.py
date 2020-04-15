def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            print(arr)
            if arr[j] > arr[j+1]:
                # temp = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = temp
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



print(bubbleSort([13,22,43,54,35,46,7]))