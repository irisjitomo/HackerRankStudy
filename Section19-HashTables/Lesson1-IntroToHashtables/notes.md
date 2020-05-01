# Hash Tables
    - Also known as Hash Maps

# Objectives  
    - Explain what a hash table is 
    - Define hashing algorithm
    - Discuss what makes a good hashing algorithm
    - Understand how collsions occur
    - How to deal with collisions

# What is a hash table?

    - Hash tables are used to store `key-value` pairs

    - They are like arrays, but the keys are not ordered

    - Unlike arrays, hashtables are fast for all operations

# Why should I care?

    - Nearly every programming language hash some sort of hash table data structure

    - Because of their speed, hash tables are very commonly used

# Hash Tables in the wild
    - Python - Dict()
    - JS - Objects and Maps*
    - Java, Go, and Scala have Maps
    - Ruby has... Hashes

*********************************************************************************

# Introductory Example:

- Imagine we want to store some colors, We could just use an array/list:

colors = ['#ff69b4', '#ff4500', '#00ffff']

- Not super readable! What do these colors correspond to?

- It would be better to use human readable keys

# pink ----> #ff69b4
# orangered ----> #ff4500
# cyan ----> #00ffff

colors['cyan'] is WAY BETTER than colors[2]


# What's the goal in this section?

Reinvent key-value pairs


# How can we get human-readability and computer readability?

- Hash tables are to the rescue!

