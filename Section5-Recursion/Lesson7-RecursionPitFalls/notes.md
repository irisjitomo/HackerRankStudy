# Common PitFalls in recursion - Where things can go wrong

# Wrong or nonexistent base case

# For Example with the recursion factorial problem

    def recursive_factorial(num):
        if num == 1:
            return 1
        return num * recursive_factorial(num - 1)
 
  **Let's say that we didnt have a base case**

    def recursive_factorial(num):
        return num * recursive_factorial(num - 1)

- `num` would go into the infinity negative numbers. Why? We never had a base case that stops that recursive_factorial.

# Another Example: forgetting to `return` or wrong `return` or printing OR console.log instead of `return`

    def recursive_factorial(num):
        if num == 1:
            return 1
        return num * recursive_factorial(num) <--- **this would run infinitely because we dont manipulate the new input**


# ALL OF THESE CAN RESULT IN WHATS CALLED A 'STACK OVERFLOW'