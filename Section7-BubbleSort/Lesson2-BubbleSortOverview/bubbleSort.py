def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1): # this ensures that we only loop 
            # - 1 after the pass in completed. So we never touch the sorted
            # numbers on the right side of the list
            print(arr, arr[j], arr[j+1])
            if arr[j] > arr[j+1]:
                # temp = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = temp
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("one pass completed")
    return arr



print(bubbleSort([13,22,43,54,35,-46,7]))