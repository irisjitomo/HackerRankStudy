Step 5 - Look back and Refactor


- Can you check the result?
- Can you derive the result differently?
- Can you understand it at a glance?
- Can you use the result or method for some other problem?
- Can you improve the perdformance of your solution?
- Can you think of other ways to refactor?
- How have other people solved this problem?


*** My first pass solition: ***


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


*** My refactored pass solition: ***


def charCount(string):
    chars = dict()
    for i in string.lower(): *** getting rid of new_string variable and just lowercasing the string parameter itself ***
        if i.isspace() is False and i.isalnum() is True: *** checking if i (char) is already alphanumeric ***
            if i not in chars.keys():   *** thus making the code more DRY ***
                chars[i] = 1
            else: *** chenged elif to else ***
                chars[i] += 1
    return chars
