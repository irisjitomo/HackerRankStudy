'''
Implement function countUniqueValues

accepts a sorted array, and counts the unique values in the array. 
There can be negative numbers in the array. but it will always be sorted
'''

def countUniqueValues(arr):
    if len(arr) == 0:
        return 0
    # sort array
    arr.sort()
    # establish a counter
    count = 0
    # make 2 pointers, starting at 0 and one starting at index 1
    first = 0
    second = 1
    # iterate over arr (while loop)
    while second < len(arr):
        # print(arr[first], '/', arr[second])
        if arr[second] != arr[first]:
            count += 1
        first += 1
        second += 1
    return count + 1

arr0 = []
arr = [1,1,1,2,2,3,4,4,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9,1,1,10,12, 199191]

print(countUniqueValues(arr))


# Udemy Solution

def countUniqueValuesSolution(arr):
    arr.sort()
    if len(arr) == 0:
        return 0
    # we make an `i` pointer
    i = 0
    # we make another `num` pointer that is +1 index
    for num in range(1, len(arr), 1):
        # if value in index `i` is not equal to val in index `num`
        # we have found a unique value
        if arr[i] != arr[num]:
            # we increment the `i` index
            i += 1
            # whatever value was in index `num` will be the new value in
            # index `i`
            # `num` keeps moving since it is in a for loop
            arr[i] = arr[num]
    # we return the count of `i` + 1 since that determines the 
    # count of unique values
    return i + 1


print(countUniqueValuesSolution(arr))
