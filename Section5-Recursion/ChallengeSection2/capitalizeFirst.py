'''
Given an arr of strings, capitalize the first letter of each string in array
'''

def capitalizeFirst(arr):
    new_arr = []
    # if len of arr == 0 return arr
    if len(arr) == 0:
        return new_arr
    # we need to access not only the index of arr, but first letter in that string
    # so maybe like arr[index[0]]
    # and then capitalize that index
    # return capitalizeFirst(arr[1:])
    new_arr.append(arr[0].capitalize())
    return new_arr + capitalizeFirst(arr[1:])


    # return arr[0]
    # str = arr[0]
    # return str[0].upper()

print(capitalizeFirst(['hello', 'nice', 'cool']))