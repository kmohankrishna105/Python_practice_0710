def square(num):
    return num**2

my_nums = [1,2,3,4,5]

print(map(square,my_nums))

# To get the results, either iterate through map()
# or just cast to a list
print(list(map(square,my_nums)))