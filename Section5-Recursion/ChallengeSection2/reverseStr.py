'''
Write a function `reverse` that takes a string and returns a new string in reverse
'''

def reverse(str):
    if len(str) <= 1:
        return str
    return str[1:] + str[0]

print(reverse('hello'))


# def reverse(arr):
#     # # make a new list, that will store the chars in as vals
#     # new_arr = []
#     # # base case: if len(arr) == 0
#     # if len(arr) == 0:
#     #     # return new_arr
#     #     return ''.join([str(char) for char in new_arr])
#     # # append char in new_arr
#     # new_arr.append(arr[-1])
#     # # return new_arr + reverse(arr[:-1])
#     # return new_arr + reverse(arr[:-1])

#     new_arr = arr
#     return ''.join([str(char) for char in new_arr])


# arr = ['h', 'e', 'l', 'l', 'o']
# print(reverse(arr))