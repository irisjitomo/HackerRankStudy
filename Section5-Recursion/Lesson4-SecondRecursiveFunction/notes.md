# Second Recursive Example

    def sumRange(num):
        if num == 1:
            return 1
        return num + sumRange(num-1)

- We call sumrange(3), and it will return 3 + sumRange(3-1)

- then we call sumRange(2) and it will return 2 + sumRange(2-1)

- then we call sumRange(1), we stop because its the base case

sumRange(3)
    return 3 = sumRange(2)
        return 2 + sumRange(1)
            return 1

# It'll look like this now

sumRange(3)
    return 3 + sumRange(2)
        return 2 + 1  <----- This sumRange(1) turned to 1 because it returned 1

# Then...

sumRange(3)
    return 3 + 3 <---- This is 3 because from the previous line it returned 2 + 1 which is 3

# Then...  it will return 6 because 3 + 3 is 6