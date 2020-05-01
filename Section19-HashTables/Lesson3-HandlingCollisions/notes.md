# Dealing With Collisions

- Even with a large array and a great hash function, collisions are inevitable

- There are many strategies for dealing with collisions, but we'll focus on two:
    1. Separate Chaining
    2 . Linear Probing

***************************************

# Separate Chaining
    - With separate chaining, at each index in our array, we store values using a more sophisticated data structure

    - This allows us to store multiple key-value pairs in a single index

# Example 

darkblue ---> 4
salmon ----> 4

This is what index 4 would look like: 
[['darkblue', '#00008b'], ['salmon', '#fa8072']]

This can be a linked list

# Linear Probing
    - Basically looking ahead of that index, seeing if there are free spots in the succeeding indices