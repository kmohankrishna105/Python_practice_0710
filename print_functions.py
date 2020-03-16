"""


The oldest method involves placeholders using the modulo % character.
An improved technique uses the .format() string method.
The newest method, introduced with Python 3.6, uses formatted string literals, called f-strings.

"""

#Concept 1:
print("I'm going to inject %s here." %'something')
print("I'm going to inject %s text here, and %s text here." %('some','more'))


x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))


#Padding and Precision of Floating Point Numbers
print('Floating point numbers: %25.2f' %(13.144))
print('Floating point numbers: %1.5f' %(13.144))

#Concept 2:
print('This is a string with an {}'.format('insert'))
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))


#Concept 3:

name = 'Fred'
print(f"He said his name is {name}.")

num = 23.45

print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")

