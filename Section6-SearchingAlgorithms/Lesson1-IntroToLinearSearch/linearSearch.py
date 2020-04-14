'''
PseudoCode:
- function accepts an array and a value
- loop through entire arrayand check if the current array element is equal to the value
- if it is, return the index at which the element is found
- if the value is not there, return -1
'''

def linearSearch(arr, val):
    index = 0
    for i in arr:
        if i == val:
            return index
        elif i not in arr:
            return -1
        index += 1

print(linearSearch([1,2,3,4,5], 2))
