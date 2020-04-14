def charCount(str):
    # make dict to return at end
    char_counter = {}
    # loop over string
    for char in range(0, len(str)):
        # if char is letter/num AND a key in dict, add one to count
        if str[char].isalnum() and str[char] in char_counter.keys():
            char_counter[str[char].lower()] += 1
        # elif char is letter/num AND a key NOT in dict, set value to 1
        elif str[char].isalnum() and str[char] not in char_counter.keys():
            char_counter[str[char].lower()] = 1
        # otherwise char is something else, dont do anything
        else:
            continue

    # return dict at end
    return char_counter

print(charCount('hellohell   oh12352   3423!@#$#%^&%&%^4elloh  ellohe  llohello'))