# Sliding Window

- This pattern involves creating a `window` which can either be an array or number from one position to another

- Depending on a certain condition, the window either increases or closes (and a new window is created)

- Very useful for keeping track of a subset of data in an array/string etc.

# Example: Find longest string of unque characters

`hellothere` // returns `lother`

# Another Example: Write a function called maxSubarraySum which accepts an `array of ints` and a `target` number. The function should calculate the maximum sum of `n` consecutive elements in the array.

# Basically, whatever pair creates the largest sum, that is the sum that will be returned

maxSubarraySum([1,2,5,2,8,1,5], 2) // returns 10 because 2 in arr[3] creates the biggest sum with 8 in arr[4]. We only want the sum of `TWO` consecutive nums

maxSubarraySum([1,2,3,4,5,6,7,8], 3) // returns 21 since 6 + 7 + 8 is the biggest sum from `THREE` consecutive nums


# Sliding Window Approach:
- We can add up the first 3 nums and keep that sum as a temp var
- When we keep moving in the for loop, we can keep moving through and rather
than adding up the next three digits again, we can subtract the first num and 
then add the num after the 3rd digit

# Example: ([1,2,3,4],3)
The sum of the first 3 is 6, then we need to move by one
We then subtract 1 from 6, and then we add the num in the next index, which is 4.
9 is the new larger sum
This is basically `Sliding`

    def maxSubArraySumSlidingWindow(arr, num):
        if len(arr) < num:
            return None
        maxSum = 0
        tempSum = 0
        for i in range(0, num, 1):
            # the maxSum += arr[i]
            maxSum += arr[i]
        print('maxSum', maxSum)
        tempSum = maxSum
        for i in range(num, len(arr), 1):
            print(arr[i], '/', arr[i - num])
            tempSum = tempSum - arr[i - num] + arr[i]
            print(tempSum)
            maxSum = max(maxSum, tempSum)
        return maxSum

- make edge case if len(arr) < num, return None
- make 2 vars, the tempSum and the maxSum
- loop through the FIRST num (whatever num is) and add them up, then make that to be the new maxSum
- we make the tempSum to be that maxSum
- loop again
    - this time we make the tempSum to tempSum minus index - num then add
    the index since that is the next number in the loop
    - then the new maxSum will be when we max() the maxSum and the tempSum
    - Now with max() were basically comparing the maxSum to the tempSum, we take the larger number
- return maxSum