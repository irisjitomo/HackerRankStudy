# Merge Sort

# Why learn this? 
- Merge sort and the other sorting algos after this is MUCH faster than selection, bubble, insertion sort.
- Improves time complexity from 0(n**2) to 0(n log n)

# Merge Sort

- Its a combination of two things, merging and sorting
- Exploits the fact that arrays of 0 to 1 element are always sorted
- Works by decomposing an array into smaller arrays of 0,1 elements, then bulding up a newly sorted array

# How does it work?

[ 8, 3, 5, 4 ,7, 6, 1, 2 ] we split it

[ 8, 3, 5, 4 ] and [ 7, 6, 1, 2 ]

[ 8, 3 ] and [ 5, 4 ] and [ 7, 6 ] and [ 1, 2 ]

then ...

[ 8 ] and [ 3 ] and [ 5 ] and [ 4 ] and [ 7 ] and [ 6 ] and [ 1 ] and [ 2 ]

