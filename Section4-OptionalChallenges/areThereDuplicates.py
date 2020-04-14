'''
Implement a function which accepts a variable number of args, checks whether there are any duplicates among the arguments passed in.
'''

def duplicates(arr):
    # make multiple pointers starting at 0 and starting at index 1
    arr.sort()
    pointer1 = 0
    pointer2 = 1
    while pointer2 < len(arr):
        if arr[pointer1] == arr[pointer2]:
            return True
        else:
            pointer1 += 1
            pointer2 += 1
    return False

print(duplicates([1,2,3,4,2]))
print(duplicates([1,2,3,4]))