Step 2 - Concrete Examples

- Coming up with examples can help you understand the problem better

- Examples also provide sanity checks that your eventual solution works how it should

                    User Stories!       Unit Tests!

- Start with Simple Examples
- Progress to more complex examples
- Explore Examples with Empty Inputs
- Explore Examples with Invalid Inputs


Example:
    Write a function which takes in a string and return the count of each character in the string


charCount('aaaa') ----> {a:4}
charCount('hello') ----> {h:1, e:1, l:2, o:1}


- Progress to more complex examples

charCount('my phone number is 182763') // do we count the spaces? do we count the numbers?
charCount('Hello hi') // do we ignore upper/lowercasings?


- Explore examples with empty inputs

charCount('') // do we want to return False? 

- Explore examples with invalid inputs

charCount(123) // do we return False since its not a string?