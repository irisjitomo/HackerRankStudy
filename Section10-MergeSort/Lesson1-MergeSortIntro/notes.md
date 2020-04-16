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

[ 8, 3, 5, 4 ] `and` [ 7, 6, 1, 2 ]

[ 8, 3 ] `and` [ 5, 4 ] `and` [ 7, 6 ] `and` [ 1, 2 ]

then ...

[ 8 ] `and` [ 3 ] `and` [ 5 ] `and` [ 4 ] `and` [ 7 ] `and` [ 6 ] `and` [ 1 ] `and` [ 2 ] `this is when we merge`

[ 3, 8 ] `and` [ 4, 5] `and` [ 6, 7 ] `and` [ 1, 2 ] `then we put them together`

*But before we sort them together we have to compare the items, take the `first item` then `compare` to the `second array's first item`, whatever is smaller, put that one first in the new array, then compare `second item` with the `second array's first item` then whatever is smaller, put that one first then same thing in that order*

[ 3, 4, 5, 8 ] `and` [ 1, 2, 6, 7]

[ 1, 2, 3, 4, 5, 6, 7, 8 ]

... In a nutshell, we're basically splitting and merging ...

