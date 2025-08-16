# A tuple looks just like a list except you use parentheses instead of square
# brackets. Once you define a tuple, you can access individual elements by
# using each item’s index, just as you would for a list.

dimensions = (200 , 50)
print(dimensions[0])
print(dimensions[1])

# modifying a tuple . Although you can’t modify a tuple, you can assign a new value to a variable
# that represents a tuple. So if we wanted to change our dimensions, we could
# redefine the entire tuple:

dimensions = (200 , 50)
print('\nthe original dimension is = ')
for dimension in dimensions:
    print(dimension)

dimensions=(400 , 500)
print("\nThe modified list is = ")
for dimension in dimensions:
    print(dimension)


# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed throughout the life of a program.