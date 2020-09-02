# NAIVE APPROACH

import math 


def maxsum(arr, n):
    if len(arr) < n:
        return None
    max = -math.inf
    for i in range(0,len(arr) - n + 1, 1):
        temp = 0
        for j in range(0, n, 1):
            temp += arr[i + j]
            if max < temp:
                max = temp
    return max 



arr1 = [2,6,9,2,1,8,5,6,3]
# print(maxsum(arr1, 3))


# SLIDING WINDOW APPROACH

def maxSumWindow(arr, n):
    maxSum = 0
    tempSum = 0
    if len(arr) < n:
        return None
    for i in range(0, n, 1):
        maxSum += arr[i]
    tempSum = maxSum
    for i in range(n, len(arr), 1):
        print(arr)
        print('add', arr[i], 'to tempSum, which is index:', i, 'and arr[i-n] is:', arr[i-n], 'and we subtract it from tempSum')
        tempSum = tempSum - arr[i - n] + arr[i]
        print('new tempSum: ', tempSum)
        print('        ')
        maxSum = max(maxSum, tempSum)
    return "maxSum:", maxSum

arr12 = [2,6,9,2,1,8,5,6,3]


print(maxSumWindow(arr12, 3)) 