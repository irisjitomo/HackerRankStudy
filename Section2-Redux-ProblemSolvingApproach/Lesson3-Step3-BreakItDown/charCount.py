

def charCount(string):
    chars = dict()
    new_string = string.lower()
    for i in new_string:
        if i.isspace() is False and i.isalnum() is True:
            if i not in chars.keys():
                chars[i] = 1
            elif i in chars.keys():
                chars[i] += 1
    return chars



print(charCount('Hello123   321 yes sir!!!'))