# Binary Search Pseudocode

- function accepts a `sorted` array and a value
- Create a left and right pointer
- `While` the left pointer comes before the right pointer
- middle pointer will be left - right // 2
- if middle == val, return `the index`
- if val is too small, left = middle + 1
- if val is too large, right = middle - 1
- return -1 if val is not found