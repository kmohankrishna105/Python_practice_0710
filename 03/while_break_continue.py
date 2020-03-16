"""
while test:
    code statements
else:
    final code statements

"""

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1

#===============Break continue,Pass
"""
while test: 
    code statement
    if test: 
        break
    if test: 
        continue 
else:

"""

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing...')
        continue



#==========Break

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue

#==============DANGER
# DO NOT RUN THIS CODE!!!!
while True:
    print("I'm stuck in an infinite loop!")

