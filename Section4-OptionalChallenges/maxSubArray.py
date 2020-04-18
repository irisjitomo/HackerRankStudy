'''
Return a subarray of consecutive numbers with the largest sum
'''

def maxSubArray(arr, num):
    if len(arr) < 0:
        return None
    # make a max value
    maxSum = 0
    # make subArray to contain those elems
    # make a window containting two elements in the array
    for i in range(0, num, 1):
        maxSum += arr[i]
    tempSum = maxSum
    for i in range(num, len(arr), 1):
        print(arr[i], '/', arr[i - num])
        tempSum = tempSum - arr[i - num] + arr[i]
        maxSum = max(maxSum, tempSum)

    # save the sum of those two elements in the array, and keep going
    # when we get to the end of the array, return the subarray containing the
    # elements that summed up `max`
    return maxSum

print(maxSubArray([1,2,3,4,5],3))
print(maxSubArray([100,200,300,400], 2))