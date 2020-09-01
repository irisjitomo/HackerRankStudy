'''
Anagrams 

Given two strings, write a func to determine if the second string is an anagram of the first.

'''


def validAnagram(str1, str2):
    '''
    using 2 dicts
    '''
    # counter1 = {}
    # counter2 = {}
    # if len(str1) != len(str2):
    #     return False
    # for i in str1:
    #     if i not in counter1:
    #         counter1[i] = 1
    #     else:
    #         counter1[i] += 1
    # for i in str2:
    #     if i not in counter2:
    #         counter2[i] = 1
    #     else:
    #         counter2[i] += 1
    # # first check to see if the keys are the same in both dicts
    # for letter in counter1.keys():
    #     if letter not in counter2.keys():
    #         return False
    # # check to see if the keys have the same amount of values
    #     elif counter1[letter] != counter2[letter]:
    #         return False
    # # return true
    # return True
    '''
    using one dict, subtracting from a dict values
    '''
    letters = {}
    if len(str1) != len(str2):
        return False
    for i in str1:
        if i not in letters.keys():
            letters[i] = 1
        else:
            letters[i] += 1
    for letter2 in str2:
        if letters[letter2] < 0:
            return False
        else:
            letters[letter2] -= 1
    return True


print(validAnagram(' ', ' '))
print(validAnagram('helo ', 'lohe'))
print(validAnagram('hello', 'llohe'))
print(validAnagram('helo2', 'lohe'))