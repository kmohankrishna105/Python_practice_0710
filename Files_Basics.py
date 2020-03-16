#myfile = open('whoops.txt')


# Open the text.txt
my_file = open('test.txt')

# We can now read the file
my_file.read()


# Seek to the start of file (index 0)
my_file.seek(0)


# Now read again
my_file.read()


# Readlines returns a list of the lines in the file
my_file.seek(0)
my_file.readlines()

#===============================================Writing to a file
# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file
my_file = open('test.txt','w+')


#'w' or 'w+' truncates the original
# Write to the file
my_file.write('This is a new line')

#===================Appending to a File¶=======================
my_file = open('test.txt','a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')


#=======================Iterating through a File=================
for line in open('test.txt'):
    print(line)


