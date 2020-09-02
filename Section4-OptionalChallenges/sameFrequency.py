'''

def sameFrequency:

a Function that takes two nums, if the frequency of digits in num1 matches the num2 digits, return True

examples:

num_a = 123 and num_b = 321, it would return True

num_c = 123456 and num_d = 765432, it would return False

num_e = 967845 and num_f = 785469, it would return True

Try to think of edge cases, things to look for that would automatically make it return False

'''

def sameFrequency(num1,num2):
    if len(str(num1)) != len(str(num2)):
        return False
    # make a dict to store frequency
    dict = {}
    for i in str(num1):
        if i not in dict.keys():
            dict[i] = 1
        elif i in dict.keys():
            dict[i] += 1
    # loop through num2
    for j in str(num2):
        # check if it is in the keys()
        if j in dict.keys():
            # check if the frequencies are the same
            dict[j] -= 1
            print(dict)
            if dict[j] < 0 or dict[j] > 0:
                return False
    return True
    
        

print(sameFrequency(1232261,2373112))
print(sameFrequency(4567777,7444465))
print(sameFrequency(123,321))
print(sameFrequency(34,14))