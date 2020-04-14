''' 
Given two strings, write a function to determine if the second string
is an ANAGRAM of the first. The number of letters must match (frequency pattern).
Return True or False
'''

'''
test examples:
validAnagram('','') // true
validAnagram('aaz', 'zza') // false
validAnagram('anagram', 'nagaram') // false
'''

def validAnagram(str1, str2):
    # check if len of str same
    if len(str1) != len(str2):
        return False
    # make a dict to store chars and counters
    chars = {}
    # loop through first string
    for i in str1:
        # if not a key then add as key with a val of 1
        if i not in chars.keys():
            chars[i] = 1
        # increment val by 1 if key exists
        elif i in chars.keys():
            chars[i] += 1
    print(chars)
    # loop through 2nd string
    for j in str2:
        # if that char is not a key inside our chars dict, return False
        if j not in chars.keys():
            return False
        # we need to check if the frequency is the same so we have to
        # check that by reducing the freq by 1. If its the same frequency,
        # it will skip this else block
        elif j in chars.keys():
            chars[j] -= 1
            if chars[j] < 0:
                return False
    return True

print(validAnagram('hellol', 'oolleh'))