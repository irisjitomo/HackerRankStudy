# Space Complexity

so far we've been focusing on `time complexity`: how can we analyze the runtime of an algorithm as the size of input increases

# using big 0

we can also use big 0 notation to analyze `space complexity`: how much additional memory do we need to allocate in order to run the code in our algorithm

# Space Complexity in JS Rules of Thumb:

- Most primitives (booleans, numbers, undefined, null) are constant space
- String require 0(n) space (where `n` is the string length)
- Reference types are generally 0(n) where `n` is the lenth for arrays or the number of keys in objects

# an example, sum up an array:

    def sum(arr):
        total = 0
        for i in arr:
            total += i
        return total
    
what are the things that take up space? We have one number `total`. We also have another number that we declared inside the forloop `i`. We have two numbers, thats our space. We have `constant space` cause we have `constantly two variables`. `We add on to the vars`, but `never add other vars`. So `0(1)` is our space complexity.

# another example, double nums in arr:

    def double(arr):
        new_arr = []
        for i in arr:
            new_arr.append(i * 2)
        return new_arr

we have to notice that we have a `new_arr` array, as long as the for loop runs, it will `keep adding on to that new_arr`. But the new_arr length will always be proportionate to the `n` or `arr` array. This is `0(n)` since were adding more nums to a new array