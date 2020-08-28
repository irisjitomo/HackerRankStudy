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
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        temp = arr[i]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr

print(selectionSort([2342342,5673,6346,1543,1022342,345345,356456,2342]))