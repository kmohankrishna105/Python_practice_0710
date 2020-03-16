
print(list(range(0,11)))

"""enumerate"""
index_count = 0
for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1


# Notice the tuple unpacking!
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

"""Zip"""

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

# This one is also a generator! We will explain this later, but for now let's transform it to a list
zip(mylist1,mylist2)
print(list(zip(mylist1,mylist2)))


"""in"""

print('x' in ['x','y','z'])

"""min,max"""

mylist = [10,20,30,40,100]
min(mylist)
max(mylist)

"""random"""
from random import shuffle
# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
shuffle(mylist)
print(mylist)

from random import randint
# Return random integer in range [a, b], including both end points.
print(randint(0,100))

# Return random integer in range [a, b], including both end points.
print(randint(0,100))


"""input"""

print(input('Enter Something into this box: '))