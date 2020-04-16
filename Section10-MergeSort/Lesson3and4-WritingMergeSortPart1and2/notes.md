# Writing Merge Sort Part 1:

# mergeSort pseuodocode (uses recursion):
- Break up the array into halves until you have arrays that are empty or have one elements, use array slicing
- call mergeSort again to keep slicing
- base case: when array length == 1 or 0

- Once you have smaller sorted arrays, `merge those arrays with their sorted arrays` `until you are back at the full length of the array`