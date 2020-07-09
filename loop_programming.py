"""Interchange variable values using 3rd Variable
"""
#  Take input number from User

input_num_a = int(input("Please enter your first number --- > "))
input_num_b = int(input("Please enter your second number --- > "))

# We are using 3rd variable
c = input_num_a
input_num_a = input_num_b
input_num_b = c

# After change first value is
print("After changing value, first value is =  " + str(input_num_a))

# After change second value is
print("After changing value, second value is =  " + str(input_num_b))


"""Interchange variable values with out  using 3rd Variable
"""
#  Take input number from User

input_num_a = int(input("Please enter your first number --- > "))
input_num_b = int(input("Please enter your second number --- > "))

# We are not using 3rd variable

input_num_a = input_num_a + input_num_b
input_num_b = input_num_a - input_num_b
input_num_a = input_num_a - input_num_b

# After change first value is
print("After changing value, first value is =  " + str(input_num_a))

# After change second value is
print("After changing value, second value is =  " + str(input_num_b))



#  Print * Rectangle

for i in range(1, 6):
    for j in range(1, 6):
        print("*",
              end='')  # By default line ended with new line, here we define, nothing to be added at the end of line
    print()



"""
Practical
Programming - 4: Write
program
to
find
factorial
of
a
number
"""
#  Take input from User and generate factorial result
z = 1
x = int(input("Please enter your number :  - "))
while (x > 0):
    z = z * x
    x = x - 1
print("Factorial result is : " + str(z))

"""Practical
Programming - 5: Write
program
to
Generate
Fibonacci
series
"""

#  Take input from User and generate fabonnaci series

x = int(input("Please enter your number :  - "))

#  Define initial 2 values
a = 0
b = 1
print(a)
print(b)
while ((a + b) < x):
    b = a + b
    a = b - a
    print(b)

