"""

1.) Constructing Tuples
2.) Basic Tuple Methods
3.) Immutability
4.) When to Use Tuples

"""

# Create a tuple
t = (1,2,3)
print(len(t))


# Can also mix object types
t = ('one',2)
# Show
print(t)

# Use indexing just like we did in lists
print(t[0])

# Slicing just like a list
print(t[-1])


print(t.index('one'))

# Use .count to count the number of times a value appears
print(t.count('one'))