# Insertion Sort

- Builds up the sort by gradually creating a larfer left half which is always sorted

Example:
[5,3,4,1,2] 
[3,5,4,1,2] first pass
[3,4,5,1,2] second pass
[1,3,4,5,2] third pass
[1,2,3,4,5] fourth pass


# Insertion sort pseuodocode
- Start by picking the second element in the array
- Now compare the second element with the one before it and swap if necessary
- Continue to the next element and if it is in the incorrect order, iterate through the sorted portion(i,e, the left side) to place the lement in the correct place.