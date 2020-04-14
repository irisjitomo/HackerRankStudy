def logAtLeast5(n):
        for i in range(1, max(5+1, n+1), 1):
            print(i)

logAtLeast5(7)
print('-----')

def logAtMost5(n):
    for i in range(1, min(5+1, n+1), 1):
        print(i)

logAtMost5(7)