# First Recursive Function Writing

# How recursive functions work

- Invoke the `same` function with a different input until you reach your `base case`

# What is the base case?

- The `condition` when the recursion ends.

**THIS IS THE MOST IMPORTANT CONCEPT TO UNDERSTAND**

# Two Essential parts of a recursive function
    - Base Case
    - Different input

# First recursive function: Countdown

    def countDown(num):
        if num <= 0:
            print('All Done')
            return
        print(num)
        countDown(num - 1)