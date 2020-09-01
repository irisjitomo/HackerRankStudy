# This is the naive approach because it is n ** 2 in time complexity

def same(arr1, arr2):
    if len(arr1) == len(arr2):
        for num1 in arr1:
            num_sq = arr2.index(arr1[num1 - 1] ** 2)
            if num_sq == -1:
                return False
            print(arr2)
            arr2.pop(num_sq)
        return True

    else:
        return False

arr1 = [2,3, 2, 2]
arr2 = [9,4,4,4]
arr3 = [4,3,4,5]

arr4 = [10, 2, 4, 6]
arr5 = [4, 16, 36, 100]


# print(same(arr1, arr2))

# Refactored Approach. This is 0(n) or 0(3n):

def same_refactored(arr1, arr2):
    freq_counter1 = {}
    freq_counter2 = {}
    if len(arr1) != len(arr2):
        return False
    for num1 in arr1:
        if num1 in freq_counter1.keys():
            freq_counter1[num1] += 1
        elif num1 not in freq_counter1.keys():
            freq_counter1[num1] = 1
    for num2 in arr2:
        if num2 in freq_counter2.keys():
            freq_counter2[num2] += 1
        elif num2 not in freq_counter2.keys():
            freq_counter2[num2] = 1
    print(freq_counter1, freq_counter2)
    for val1 in freq_counter1.keys():
        if not val1 ** 2 in freq_counter2.keys():
            return False
        elif freq_counter2[val1 ** 2] != freq_counter1[val1]:
            return False
        else:
            return True
        

print(same_refactored(arr3, arr5))
