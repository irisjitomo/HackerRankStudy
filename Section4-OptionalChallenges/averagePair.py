''' 
Given a sorted arr of ints and a target average. Determine if the `average` of the pair of values is equal to the target `average`.
`average` is two nums / 2
'''

# def averagePair(arr, average):
#     arr.sort()
#     if len(arr) < 2:
#         return False
#     start = 0
#     next = 1
#     while next < len(arr):
#         pair_average = (arr[start] + arr[next]) / 2
#         if pair_average == average:
#             print([arr[start], arr[next]])
#             return True
#         elif pair_average < average:
#             start += 1
#         else:
#             next += 1

    # return False

def averagePair(arr, average):
    arr.sort()
    if len(arr) < 2:
        return False
    start = 0
    end = len(arr) - 1
    while start < end:
        pair_av = arr[start] + arr[end] / 2
        if pair_av == average:
            print(arr[start], arr[end])
            return True
        elif pair_av < average:
            start += 1
        end -= 1
    return False



# print(averagePair([1,2,3], 2.5))
print(averagePair([1,3,3,5,6,7,10,12,19], 6.5))
# print(averagePair([55,1,6,10,15,26,11],12.5))