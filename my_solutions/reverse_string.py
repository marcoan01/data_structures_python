"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.
for char in string:
    s.push(char)

while s.isEmpty() != True:
    reversed_string = reversed_string + s.pop()

print(reversed_string)

