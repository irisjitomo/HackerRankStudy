'''
Write a function, where given two positive integers, find out if the two nums have the same frequent of digits

examples:
(123, 456) // true
(12, 1234) // false
(123456, 198765) // true
'''

def sameFreq(num1, num2):
    if len(str(num1)) != len(str(num2)):
        return False
    counter = dict()
    for i in str(num1):
        if i not in counter.keys():
            counter[i] = 1
        else:
            counter[i] += 1
    for i in str(num2):
        if i in counter.keys():
            counter[i] -= 1
        else:
            return False
    return True


print(sameFreq(123, 321))
print(sameFreq(34, 14))
print(sameFreq(3589578, 5879385))
print(sameFreq(22, 222))