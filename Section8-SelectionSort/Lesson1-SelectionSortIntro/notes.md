# Selection Sort

- Similar to bubble sort, but `instead of first placing large values` into sorted postion, `it places small values into sorted position`

# Steps

- we start at arr[0] and that will be our minimum
- we keep moving until we find one that is smaller than arr[0], if there is a value smaller than arr[0], we make that our new minimum
- at the end of the loop, whatever is our smallest element, we swap with arr[0]

# Pseudocode

- Store the first element as the smallest val so far
- Compare this item to the next items in array until you find a smaller num
- once we find that smaller num, we save the INDEX so we can swap index of 0 with whatever the index is of the new minimum number