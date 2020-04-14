# Multiple Pointers: Count Unique Values Challenge

# Implement function countUniqueValues

- accepts a sorted array, and counts the unique values in the array. There can be negative numbers in the array. but it will always be sorted

# My Solution:

    def countUniqueValues(arr):
        if len(arr) == 0:
            return 0
        arr.sort()
        count = 0
        first = 0
        second = 1
        while second < len(arr):
            if arr[second] != arr[first]:
                count += 1
            first += 1
            second += 1
        return count + 1

- sort array
- establish a counter
- make 2 pointers, starting at 0 and one starting at index 1
- iterate over arr (while loop)


# Udemy Solution:

    def countUniqueValuesSolution(arr):
        arr.sort()
        if len(arr) == 0:
            return 0
        i = 0
        for num in range(1, len(arr), 1):
            if arr[i] != arr[num]:
                i += 1
                arr[i] = arr[num]
        return i + 1

- we make an `i` pointer
- we make another `num` pointer that is +1 index
    - if value in index `i` is not equal to val in index `num`
    we have found a unique value
        - we increment the `i` index
        - whatever value was in index `num` will be the new value in
        index `i`
        - `num` keeps moving since it is in a for loop
    - count of unique values