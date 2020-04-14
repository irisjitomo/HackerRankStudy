# Motivate the need for Big 0 notation:
________________________________________

# Whats the idea?
    Imagine we have multiple implementations of the same function, how do we know which one is 'best'?
# Who cares?
    Its important to have aprecise vocab to talk about how code performs
    Useful for discussing tradeoffs between different approaches
    Useful for debugging, whats slowing down the code? We can pinpoint inefficient parts
_________________________________________

# Lesson 1: Timing Our Code
Example: suppose we want to write a function that sums up nums from 1
up to, including, some number n

There are two functions, but which one is better?
The first or the second function