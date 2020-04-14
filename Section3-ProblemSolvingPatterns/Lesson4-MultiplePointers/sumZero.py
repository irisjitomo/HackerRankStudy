'''
accepts a `sorted` array of integers. 
The function should find the `first` pair where the sum is 0. 
Return an array that includes both values that sum to zero 
or undefined if a pair does not exist
'''

def sumZero(arr):
    # if arr is less than 2:
        # return undefined
    if len(arr) < 2:
        return None
    # sort array
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == 0:
            return [arr[left], arr[right]]
        elif sum > 0:
            right -= 1
        else:
            left += 1

print(sumZero([-3,-2,-1,0,1,2,3,-6,6]))