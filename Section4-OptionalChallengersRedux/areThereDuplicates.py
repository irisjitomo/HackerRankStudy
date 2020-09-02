def areThereDuplicates(*argv):
    collection = {}
    for i in argv:
        if i not in collection.keys():
            collection[i] = 1
        else:
            collection[i] += 1
    for i in collection.values():
        if i > 1:
            return True
    return False


print(areThereDuplicates(1,2,3))
print(areThereDuplicates('a','a','b'))
