'''
Only return alphanumeric characters: No space and special characters
'''
# def charCount(str):
#     # make dict to return at end
#     char_counter = {}
#     # loop over string
#     for char in range(0, len(str)):
#         i = str[char].lower()
#         # if char is letter/num AND a key in dict, add one to count
#         if i.isalnum() and i in char_counter.keys():
#             char_counter[i] += 1
#         # elif char is letter/num AND a key NOT in dict, set value to 1
#         elif i.isalnum() and i not in char_counter.keys():
#             char_counter[i] = 1
#         # otherwise char is something else, dont do anything
#         else:
#             continue
#     # return dict at end
#     return char_counter

# print(charCount('!@#$#$!@!@ HELLO I AM YOUR father'))


'''
Refactored Version
'''
def charCount(str):
    # make dict to return at end
    char_counter = {}
    # loop over string
    for char in str:
        char = char.lower()
        # if char is letter/num AND a key in dict, add one to count
        if char.isalnum():
            if char in char_counter.keys():
                char_counter[char] += 1
            # elif char is letter/num AND a key NOT in dict, set value to 1
            elif char not in char_counter.keys():
                char_counter[char] = 1
            # otherwise char is something else, dont do anything
            else:
                continue
    # return dict at end
    return char_counter

print(charCount('!@#$#$!@!@ HELLO I AM YOUR father'))


'''
Return any type of characters but no space
'''
def charCountAllChars(str):
    # make a dict
    chars = {}
    # loop over the length of string
    for char in range(0, len(str)):
        i = str[char].lower()
        # if char is a key in dict, then add to count
        if not i.isspace() and i in chars.keys():
            chars[i] += 1
        # if char is not a key, add as key with val of 1
        elif not i.isspace() and i not in chars.keys():
            chars[i] = 1
        # else continue
        continue
    # return dict
    return chars

print(charCountAllChars('sdfsdfsdfsdf     sdfsdfsdf   !@&*Y&*Y&*Y@#*&Y&*!'))