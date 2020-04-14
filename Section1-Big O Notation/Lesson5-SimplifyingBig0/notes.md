# Simplfying Big 0 Expressions

    When determining the time complexity of an algorithm, there are some helpful rule of thumbs for big 0 expressions.
    we can simplfy time complexities and forget about the constants

    0(2n) can become ------> 0(n)
    0(3000) can become ----> 0(1)
    0(13n**2) can become --> 0(n**2)

# Big 0 shorthands

    1. Arithmetic operations are constant
    2. Variable assignment is constant ex. x = 100
    3. Accessing elements in array using an index is constant
    4. In a loop, the complexity is the length of the loop times the complexity of whatever happens inside of the loop

# Here is another py example:
    def logAtLeast5(n):
        for i in range(1, max(5+1, n+1), 1):
            print(i)

This code prints 1 - 5 IF `n` is less than or equal to 5, but if `n` is more than 5, print 1 - `n`. This is 0(n), as n grows, the operations
grow with `n`

# another example but reverse:
    def logAtMost5(n):
        for i in range(1, min(5+1, n+1), 1):
            print(i)
This code prints a max of 1-5, if `n` is above 5, it will not print above 5. This is different because no matter what the `n` is, it will only loop a max of 5 times. So this is 0(1)