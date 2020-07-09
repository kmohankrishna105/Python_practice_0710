"""
List comprehensions allow us to build out lists using a different notation. You can think of it as essentially a one line for loop built inside of brackets
"""
# Grab every letter in string
lst = [x for x in 'word']

# Check
print(lst)


# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]
print(lst)


lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)