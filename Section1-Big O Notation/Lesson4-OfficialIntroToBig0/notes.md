# Introducing Big 0

Big 0 Notation is a way to formalize fuzzy counting

It allows us to talk formally about how the runtime of an algorithm grows as the inputs grow, its a way of describing a relationship of the input to the runtime relative to input

an algo is 0(f(n)) if the number of simple operations the computer has to do is eventually less than a constant times f(n) as n increases

f(n) could be linear (f(n) = n)
f(n) could be quadratic (f(b) = n**2)
f(n) could be constant (f(n) = 1)
f(n) could be different entirely

# if we look at this py operation:
    def addUpTo(n):
        return n * (n + 1) / 2

theres ALWAYS 3 operations: 0(1)

# if we compare it to this py operation:
    def addUpTo(n):
        total = 0
        for i in range(n+1):
            total += i
        return total

the number of operations grow because it is bounded by n: 0(n)

# Another example, we count up from 0 to 10 and back down to 0.

    def countUpAndDown(n):
        print('Going Up')
        for i in range(1, n + 1):
            print(i)
        print('Going Down')
        for j in range(n, -1, -1):
            print(j)
        print('Back Down')

we have two for loops, so it is 0(n)

# Another example with nested loops:

    def printPairs(n):
        for i in range(n+1):
            for j in range(n+1):
                print(i,j)

This is a nested for loop, 0 (n * n) which will become 0(n**2)