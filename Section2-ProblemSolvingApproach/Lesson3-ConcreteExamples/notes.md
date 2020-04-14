# Problem Solving - Concrete Examples

Step two, explore examples...
Coming up with `examples` can `help you understand` the `problem better`.
`Examples` also `provide sanity checks` that your evential `solution works how it should`.

# Explore Examples
- Start with Simple Examples
- Progress to More Complex Examples
- Explore Examples with Empty Inputs
- Explore Examples with Invalid Inputs

# Interviewer asks: `Write a function which takes in a string and returns counts of each character in the string.`:

- `Simple` Examples
charCount('aaaa'); // should return {a:4}
charCount('hello); // should return {h: 1, e: 1, l: 2, o: 1}

- `More Complex` Examples
charCount('My phone number is 1232345') // should we account for the spaces? what about the chars not present in string?
charCount('Hello hi')// should we worry about uppercase and lowercase chars?

- Examples with `empty` inputs
charCount('') // do we return 0, null, error?

- Examples with `invalid` inputs
what if the input isn't a string? Rather its an integer, array, object, dictionary?
