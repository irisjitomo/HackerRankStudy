Multiple Pointers 

Creating **pointers** or values that correspond to an index and move towards the beginnning, middle, end considering the circumstance

Example:

Write a function called sumZero which accepts a sorted array of integers. The function should find the first pair where the sum is 0. Return an array that includes both values that sum to zero or undefined if a pair does not exist


[-1,2,3,-3,4,5]

-1 with each of  all the integers after does not make 0
2 with each of all integers in the array does not make 0
3 makes 0 with -3. The pointer was on index 2 which is element 3 and the other pointer was looking for a number that can make 0 which was -3 on index 3

Pseudocode:

sort array
make two pointers both starting at 0
make while loop, pointer1 < pointer2
if arr[pointer1] and arr[pointer2] == 0:
    return list with pointer1 and pointer 2
elif sum > 0:
    pointer2 -= 1
else:
    pointer1 += 1

return None if none are found
