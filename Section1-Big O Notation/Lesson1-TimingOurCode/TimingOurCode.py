# First function

def addUpTo(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

# second Function

def addUpTo(n):
    return n * (n + 1) / 2

print(int(addUpTo(7)))