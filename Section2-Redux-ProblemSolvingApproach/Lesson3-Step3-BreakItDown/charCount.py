

def charCount(string):
    chars = dict()
    new_string = string.lower()
    for i in new_string:
        if i.isspace() is False:
            if i.isalnum() not in chars.keys():
                chars[i] = 1
            elif i.isalnum() in chars.keys():
                chars[i] += 1
    return chars



print(charCount('Hello123   321 yes sir'))