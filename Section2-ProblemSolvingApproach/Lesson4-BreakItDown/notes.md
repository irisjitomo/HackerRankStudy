# Break It Down

Take the actual steps of the problem and write them down. You gotta communicate with yourself to what youre doing

This forces you to think about your code BEFORE you write it. Helps you catch any misunderstandings.

# Example: Write a function that takes in a string, and returns the count of each char in string
# Note, interviewer said we only have to worry about undercase alphanumeric characters

- Break it down, write the skeleton of the algo

def chatCount(str):
    # do something
    # return a dictionary with keys that are lowercase alphanumeric chars in string; values should be the count

def chatCount(str):
    // make dict to return at end
    // loop over string
    // return dict at end


charCount('Your PIN numver is 1234') // should return `{1: 1, 2: 1, 3: 1, 4: 1, b: 1, e: 1, i: 2, m: 1, n: 2, o: 1, p: 1, r: 2, s: 1, u: 2, y: 1}`