'''
PseudoCode:
- function accepts an array and a value
- loop through entire arrayand check if the current array element is equal to the value
- if it is, return the index at which the element is found
- if the value is not there, return -1
'''

def linearSearchOfIndex(arr, val):
    for i in arr:
        if arr[i] == val:
            return i
        return -1

print(linearSearchOfIndex([1,2,3,4,5], 2))
