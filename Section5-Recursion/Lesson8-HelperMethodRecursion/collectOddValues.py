def collectOddVals(arr):
    result = []

    def helper(helperInput):
        if len(helperInput) == 0:
            return
        elif helperInput[0] % 2 != 0:
            result.append(helperInput[0])
        return helper(helperInput[1:])

    helper(arr)

    if len(result) == 0:
        return('None')
    return result

print(collectOddVals([1,2,3,4,5,6,7,8,9]))
print(collectOddVals([0,2,4,6]))

# arr = [1,2,3,4,5]
# print(arr[1:])