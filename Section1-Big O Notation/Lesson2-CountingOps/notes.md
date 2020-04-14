# The problem with time:
- Different machines will record different times
- The Same machins will record different times
- For fast algos, speed measurements may not be precise enough?

# If not time, then what?
- Rather than counting seconds, we count NUMBER of OPERATIONS the machine has to do

if we look at this py operation:
    def addUpTo(n):
        return n * (n + 1) / 2

we have 1. multiplication 2. addition 3. division. So 3 operations. Only 3 Calculations

if we compare it to this py operation:
    def addUpTo(n):
        total = 0
        for i in range(n+1):
            total += i
        return total

we have more ops. We have addition, BUT its in a for loop, so that means
that `n` will determine the number of operations or the number of times the addition operation will happen. We have another operation, assigning i to be the numbers inside that for loop. Another operation which is looping however many times `n` is. We can see that there are way more operations. We also have the total += i, which is adding then comparing, so two operations.

'''
`Regardless of n, the number of operations grow roughly proportionally with n`
'''
