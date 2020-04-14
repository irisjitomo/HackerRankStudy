# Solve The Problem!!! And Simplify

Solve the problem, if you cant.... solve a simpler problem
- this means, trying to ignore the part that is giving you a hard time, in order to focus on someting else. You want to have something to show for yourself. Dont put your eggs in one basket.
- Its much better to do stuff we know how to do....

# Simplify
- Find the core difficulty in what youre trying to do.
- Temporarily ignore that difficulty
- Write a simplified solution
- Then incorporate the difficulty back in

# Lets go back to that charCount function: 

    def charCount(str):
        // # make dict to return at end
        char_counter = {}
        // # loop over string
        for char in range(0, len(str)):
            // # if char is letter/num AND a key in dict, add one to count
            if str[char].isalnum() and str[char] in char_counter.keys():
                char_counter[str[char].lower()] += 1
            // # elif char is letter/num AND a key NOT in dict, set value to 1
            elif str[char].isalnum() and str[char] not in char_counter.keys():
                char_counter[str[char].lower()] = 1
            // # otherwise char is something else, dont do anything
            else:
                continue
        // # return dict at end
        return char_counter

- Steps that we took:
    - We made a dict to return at the end
    - then we looped through the the length of the string
    - we then check if char is a key inside the dict that we made
        - if char is alphanumeric AND inside the dict as key:
            - then we add one to the count
        - elif char is alphanumeric AND char is NOT in the dict as key:
            - then we add it as key with a value of 1
        - otherwise, continue
    - then we return that dict.