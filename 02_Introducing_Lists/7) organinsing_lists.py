# to get this is order of the list to store them
# alphabetically.


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


# You can also sort this list in reverse alphabetical order by passing the
# argument reverse=True to the sort() method

cars.sort(reverse=True)
print(cars)



print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)




# printing list in reverse

pist = ['nijja' , 'pijja' , 'jijja']
pist.reverse()
print(pist)


# The reverse() method changes the order of a list permanently, but you
# can revert to the original order anytime by applying reverse() to the same
# list a second time


# find the length of the list
cars1 = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars1))