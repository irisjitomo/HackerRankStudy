

def same(arr1, arr2):
    # initialize dictionaries for freq counters
    counter1 = dict()
    counter2 = dict()
    # if/else, if len are not equal, return False,
    if len(arr1) != len(arr2):
        return False
    # else:
    # loop thru both arrays and add each value as keys in each dict() (2)
    for num1 in arr1:
        if num1 not in counter1.keys():
            counter1[num1] = 1
        else:
            counter1[num1] += 1
    for num2 in arr2:
        if num2 not in counter2.keys():
            counter2[num2] = 1
        else:
            counter2[num2] += 1
    # then loop through dictionary 1
    print(counter1, counter2)
    for number in counter1.keys():
        # if number ** 2 not in dictionary 2 keys, then return False
        if not number ** 2 in counter2.keys():
            return False
        # if the frequency value of number ** 2 in dict 2 is not the same value as number in dict 1, return False
        elif counter2[number ** 2] != counter1[number]:
            return False
    # return True
    return True    


arr_one = [1,2,3]
arr_two = [1,4,9]
arr_three = [1,2]
arr_four = [1,4,10]


print(same(arr_one, arr_four))

