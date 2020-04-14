'''
This solution is 0(n ** 2):
'''

def maxSubarraySum(arr, num):
    # if num is less than len(arr): return None
    if num > len(arr):
        return None
    max = 0
    for i in range(0, len(arr) - num + 1, 1):
        temp = 0
        for j in range(0, num, 1):
            temp += arr[i+j]
            if temp > max:
                max = temp
    return max

# print(maxSubarraySum([1,2,5,2,8,1,5,10], 2))

'''
Sliding Window Approach:
- We can add up the first 3 nums and keep that sum as a temp var
- When we keep moving in the for loop, we can keep moving through and rather
than adding up the next three digits again, we can subtract the first num and 
then add the num after the 3rd digit

Example: ([1,2,3,4],3)
The sum of the first 3 is 6, then we need to move by one
We then subtract 1 from 6, and then we add the num in the next index, which is 4.
9 is the new larger sum
This is basically `Sliding`
'''

def maxSubArraySumSlidingWindow(arr, num):
    # make edge case if len(arr) < num, return None
    if len(arr) < num:
        return None
    # make 2 vars, the tempSum and the maxSum
    maxSum = 0
    tempSum = 0
    # loop through the FIRST num (whatever num is) 
    for i in range(0, num, 1):
    # and add them up, then make that to be the new maxSum
        # the maxSum += arr[i]
        maxSum += arr[i]
    print('maxSum', maxSum)
    # we make the tempSum to be that maxSum
    tempSum = maxSum
    # loop again
    for i in range(num, len(arr), 1):
        # this time we make the tempSum to tempSum minus index - num then add
        # the index since that is the next number in the loop
        print(arr[i], '/', arr[i - num])
        tempSum = tempSum - arr[i - num] + arr[i]
        print(tempSum)
        # then the new maxSum will be when we max() the maxSum and the tempSum
        maxSum = max(maxSum, tempSum)
    # return maxSum
    return maxSum

# print(maxSubArraySumSlidingWindow([1,2,3,4,5,6,7,8], 2)) # 15
# print(maxSubArraySumSlidingWindow([1,2,3,4,5,6,7,8], 3)) # 21
# print(maxSubArraySumSlidingWindow([1,2,3,4,5,6,7,8], 4)) # 26
# print(maxSubArraySumSlidingWindow([1,2,3,4,5,6,7,8], 5)) # 30
print(maxSubArraySumSlidingWindow([10,2,4,6,4,1,1,2,3,6], 3)) # 16

