def averagePair(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        average = float((arr[left] + arr[right]) / 2.0)
        print('new iteration')
        print(arr[left], arr[right])
        print(arr[left] + arr[right])
        print('average', float((arr[left] + arr[right]) / 2.0))
        if average == target:
            return True
        elif average < target:
            left += 1
        else:
            right -= 1
    return False

print(averagePair([1,2,3], 1.5))