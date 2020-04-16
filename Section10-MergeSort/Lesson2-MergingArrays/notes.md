# Merging Arrays

- We need to implement a `function` that is responsible for `merging two sorted arrays`
- Given two arays which are sorted, `this helper function` should `create a new aray which is also sorted`, and `consists of all of the elements in the two input arrays`
- This function should run in `0(n + m) time` and `0(n + m) space` and `should not` modify the parameters passed to it


# Merging arrays pseudocode
- Create an empty array, take a look at the smallest vals in each input array
- Create two pointers, i and j, both starting at the beginning since we need to compare these two.
- While there are still untouched values (meaning while we have not reached our two array's ends)...
    - if the `value in the first array is SMALLER than the value in the second array`, `push the value in the first array into our results array` and `MOVE ON TO THE NEXT VALUE  in the FIRST array` ( look at this instruction very carefully, it involves pointer manipulation in the first array )
    - elif the `value in the first array is LARGER than the value in the second array`, `push the value in the second array into our results array` and `MOVE ON TO THE NEXT VALUE  in the SECOND ARRAY`
    - once we finish one array, we push the remaining values from the other array