def bubbleSortOptimized(arr):
    for i in range(len(arr)):
        noSwaps = True # we set True in every loop
        for j in range(0, len(arr) - i - 1): # this ensures that we only loop 
            # - 1 after the pass in completed. So we never touch the sorted
            # numbers on the right side of the list
            print(arr, arr[j], arr[j+1])
            if arr[j] > arr[j+1]:
                # temp = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = temp
                arr[j], arr[j+1] = arr[j+1], arr[j]
                noSwaps = False # But then if we do swap in this if statement: 
                # we set it to false
        if noSwaps: # if noSwaps is true, then we break out of that loop optimizing the loop
            break
        print("one pass completed") # look at this print on the terminal
        # too see how (len(arr) - i - 1) works in the for loop for j
    return arr



print(bubbleSortOptimized([13,22,43,54,35,-46,7]))
# print(bubbleSortOptimized([8,1,2,3,4,5,6,7])) # only two passes with noSwaps

# noSwaps optimize our bubble sort especially if it is nearly sorted