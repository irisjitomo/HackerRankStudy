'''
Write a function called sumZero which accepts a sorted array of integers. 
The function should find the first pair where the sum is 0. Return an array that 
includes both values that sum to zero or undefined if a pair does not exist
'''
arr1 = [-1,2,3,-3,4,5]
arr2 = [-2,0,1,3]


def sumZero(arr):
    arr.sort()
    pointer1 = 0
    pointer2 = len(arr) - 1
    while pointer1 < pointer2:
        if arr[pointer1] + arr[pointer2] == 0:
            return [arr[pointer1], arr[pointer2]]
        elif arr[pointer1] + arr[pointer2] > 0:
            pointer2 -= 1
        else:
            pointer1 += 1
    return None

print(sumZero(arr1))
print(sumZero(arr2))