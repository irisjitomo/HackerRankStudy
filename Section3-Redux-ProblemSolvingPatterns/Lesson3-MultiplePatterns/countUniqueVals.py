'''
Implement a function that accepts a sorted array and 
counts the number of unique values
'''
arr1 = [-1,2,3,-3,4,5,-1,0,5,6]


def countUniqueVals(arr):
    arr.sort()
    '''
    we can have both pointers start in the same direction and if pointer2
    doesnt match pointer1, then we add 1 to count and pointer1 and 
    pointer 2 will have the same starting point again which is where
    pointer2 left off
    '''
    count = 0
    for num in range(1, len(arr), 1):
        if arr[count] != arr[num]:
            count += 1
            # youre replacing the lement at pointer 1 at whatever element
            # youre in
            arr[count] = arr[num]
    return count + 1


print(countUniqueVals(arr1))