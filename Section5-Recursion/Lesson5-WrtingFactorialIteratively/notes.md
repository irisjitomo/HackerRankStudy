# Iterative Factorial Method:

    def factorial(num):
        total = 1
        for i in range(num, 1, -1):
            total = total * i
        return total