def collectOddVals(arr):
    oddsArr = []
    if len(arr) == 0:
        return oddsArr
    elif arr[0] % 2 != 0:
        oddsArr.append(arr[0])
    return oddsArr + collectOddVals(arr[1:])

print(collectOddVals([1,2,3,4,5,6,7,8,9]))
