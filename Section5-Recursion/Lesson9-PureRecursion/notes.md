# Pure Recursion Method

# Odd Value Array Example:

    def collectOddVals(arr):
        oddsArr = []
        if len(arr) == 0:
            return oddsArr
        elif arr[0] % 2 != 0:
            oddsArr.append(arr[0])
        return oddsArr + collectOddVals(arr[1:])

line 11 - This is where we concatentate those results with the function being called again


# Tips

- For arrays, use slicing, concatenating to return the result array that were looking for
- Strings are immutable, we need slice. Example:
    str = 'hello'
    print(str[1:4]) // prints 'ell'