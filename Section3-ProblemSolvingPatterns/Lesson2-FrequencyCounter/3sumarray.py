'''
Write a function that takes in an array, and return a 2d array of arrays
consisting 3 nums that sum up to the target valu
'''

def three_sum_arr(arr, target):
    # make a new array that will be returned
    sum_array = []
    # loop through the array 3 times
    for i in arr:
        for j in arr:
            for k in arr:
                    # if those 3 vals add up to the target,
                    if i + j + k == target:
                        new_arr = []
                        new_arr.extend([i, j, k])
                        # remove those 3 vals
                            # ?????
                        # push those 3 vals inside the new array
                        sum_array.append(new_arr)
    # return new array
    return sum_array




print(three_sum_arr([1,2,3,4,5,6] , 10))