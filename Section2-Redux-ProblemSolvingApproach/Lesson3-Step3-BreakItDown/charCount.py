

def charCount(string):
    chars = dict()
    new_string = string.lower()
    for i in string.lower():
        if i.isspace() is False and i.isalnum() is True:
            if i not in chars.keys():
                chars[i] = 1
            else:
                chars[i] += 1
    return chars



print(charCount('Hello123   321 yes sir!!!'))
