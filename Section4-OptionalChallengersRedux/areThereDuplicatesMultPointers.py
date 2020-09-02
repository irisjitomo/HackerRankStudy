def areThereDupsMultiPointers(*argv):
    args = []
    for i in argv:
        args.append(i)
    args.sort()
    left = 0
    right = 1
    while right < len(args):
        if args[left] == args[right]:
            return True
        left += 1
        right += 1
    return False
    

print(areThereDupsMultiPointers('q','a','a','b'))
print(areThereDupsMultiPointers('a','b'))