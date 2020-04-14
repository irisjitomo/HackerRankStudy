# Helper Method Recursion - Having an inner function to help the outer function

# Example: Return array of odd nums

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

- Line 8 we define the Helper Method
- Line 9 - 10 is the base case. if the lenth of arr is 0
- Line 11 - 12, if we find an odd number, we append it to results
- Line 13 - this is the recursion, we call helper again but this time we call it with the same array but sliced [1:]. So that it will keep checking iterating one element at a time in array.
- Line 15 - This is where we call that helper function