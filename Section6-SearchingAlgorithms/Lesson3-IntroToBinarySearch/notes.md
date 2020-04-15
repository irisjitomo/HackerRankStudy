# Binary Search

- Binary Search is a much faster form of search
- Rather than eliminating one element at a time, you can eliminate `half` of the remaining elements at a time
- Binary search `only works` on `sorted` arrays

# Divide and Conquer

Let's search for 15:

[1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19]
left             middle                    right

we check if 15 is less than the middle which was 11, then our new left will be 12 or middle + 1

new middle will become 17

Second pass:

we check if 15 is less than or greater than 17. Its less than so we forget about 17,18,19
left is still 12 and new right is 16.
is middle == 15?

middle == 15!