def sum(arr): # sum up nums in array
    total = 0
    for i in arr:
        total += i
    return total

# print(sum([1,2,3,4,5,6]))

def double(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i * 2)
    return new_arr

print(double([1,2,3,4,5,6]))