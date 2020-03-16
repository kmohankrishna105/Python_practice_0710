"""


1.) Constructing a Dictionary
2.) Accessing objects from a dictionary
3.) Nesting Dictionaries
4.) Basic Dictionary Methods

"""

#==================Constructing a Dictionary==================
# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}

# Call values by their key
print(my_dict['key2'])

#hold any sort of data type
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Can then even call methods on that value
print(my_dict['key3'][0].upper())

# Create a new dictionary from an empty dict
d = {}

# Create a new key through assignment
d['animal'] = 'Dog'

# Can do this with any object
d['answer'] = 42

#Show
print(d)


#==================NESTING WITH dICTIONARIES======================
# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}

# Keep calling the keys
d['key1']['nestkey']['subnestkey']

# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}

# Method to return a list of all keys
print(d.keys())


#Method to grab all values
print(d.values())

# Method to return tuples of all items  (we'll learn about tuples soon)
print(d.items())