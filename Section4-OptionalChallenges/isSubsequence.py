'''
function isSubsequence which takes in two strings and checks whether the characters in the first 
string form a subsequence of the characters in the second string. In other words,
the function should check whether the characters in the first string appear somethwere 
in the second string, without their order changing

Example:

isSubsequence('hello', 'hello world') // true
isSubsequence('sing', 'sting') // true
isSubsequence('abc', 'acb' ) // false (order matters)

'''

# def isSubsequence(str1, str2):
#     # make two pointers
#     pointer1 = 0
#     pointer2 = 0
#     # if str[pointer 1] matches str[pointer2], increment pointer 2 and 1
#     while pointer2 < len(str2):
#         if str2[pointer2] == str1[pointer1]:
#             pointer1 += 1
#         elif pointer1 == len(str1):
#             return True
#         pointer2 += 1
#     return False
#     # if pointer 2 does not match pointer1, return False
#     # return True

def isSubsequence(str1, str2):
    if len(str1) == 0:
        return True
    elif len(str2) == 0:
        return False
    elif str2[0] == str[0]:
        return isSubseequnce(str1[1:], str2[1:])
    return isSubsequence(str1, str2.slice[1:])

isSubsequence('hello', 'hello world')