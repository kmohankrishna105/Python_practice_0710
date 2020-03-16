"""


for item in object:
    statements to do stuff


"""


# We'll learn how to automate this sort of list in the next lecture
list1 = [1,2,3,4,5,6,7,8,9,10]


for num in list1:
    print(num)


for num in list1:
    if num % 2 == 0:
        print(num)


for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')



tup = (1,2,3,4,5)

for t in tup:
    print(t)


list2 = [(2,4),(6,8),(10,12)]

for tup in list2:
    print(tup)


d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)


# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v)


print(sorted(d.values()))