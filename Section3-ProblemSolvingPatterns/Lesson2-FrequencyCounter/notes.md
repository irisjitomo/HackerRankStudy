# Frequency Counters

This pattern uses objects/dicts or sets to collect values/frequencies of values

This can often avoid the need for nested loops or 0(n**2) ops with arrays/strings

# An Example:
Write a function called `same`, which `accepts two arrays`. The function should `return true` if `every val in the array has its corresponding val squared in the second array`. The `frequency of vals must be the same`.

    def same(arr1, arr2):
    
        if len(arr1) == len(arr2):      # 1
            for num1 in arr1:           # 2
                num_sq = arr2.index(arr1[num1 - 1] ** 2)    # 3
                if num_sq == -1:   # 4
                    return False
                return True

        else:
            return False

# 1: we can check for edge cases. If len of arrs is the same
# 2: we loop through arr1
# 3: we use index() where we pass in the square of num1. This is how we can check if that num1 (squared) is in any index of arr2
# 4: This is where we check if num1 sq is in any indexes of arr2. If num_sq is -1, meaning its not in there, we return False.


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

# These are the steps we took to make it 0(3n):
    - we make 2 dictionaries
    - edge case test, if len are the same
    - we loop twice through both arr1 and arr2 and make those nums as keys in their own freq_counter dict. Adding 1 if that num already exists as a kay
    - now we make a val1 temp or the keys inside the freq_counter dict, this will check for the keys in both freq_counters
    - first if statement:
        - if val1 ** 2 is NOT inside the keys of freq_counter2
    - second if statement:
        - if the amount of values matches both keys. key1 and key2 (key1 ** 2): this ensures if if theres two 2's in arr1, that would mean that are two 4's in arr2
    - return True