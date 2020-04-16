'''
# Steps

- we start at arr[0] and that will be our minimum
- we keep moving until we find one that is smaller than arr[0], 
if there is a value smaller than arr[0], we make that our new minimum
- at the end of the loop, whatever is our smallest element, we swap with arr[0]

# Pseudocode

- Store the first element as the smallest val so far
- Compare this item to the next items in array 
until you find a smaller num
- once we find that smaller num, we save the INDEX so we can swap 
index of 0 with whatever the index is of the new minimum number
'''

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr), 1): # this ensures that in another pass, we start 
            # NOT at the beginning
            # print(i, j)
            if arr[min] > arr[j]:
                print('swap', arr[min], arr[j], arr)
                arr[min], arr[j] = arr[j], arr[min]
                min = j
                print('new min: ', arr[min])
        print('completed pass')
        # print('new arr:', arr)x
        print('starting new pass')
    return arr

print(selectionSort([2342342,5673,6346,1543,1022342,345345,356456,2342]))