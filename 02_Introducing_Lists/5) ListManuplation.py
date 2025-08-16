# we can change the value of the specific element by telling its index

# also inorde to add some values to the code we need to append

list = ['ducat' , 'python' , 'hellcat']
list.append('honda')
print(list)

# we can also insert the text in list
list2 = ['apple' , 'banana' , 'pineapple' ]
list2.insert(0,'lichi')
print(list2)


# deleting an item form the list
list3 = ['honda' , 'toyota' , 'suzuki' , 'maruti']
del list3[0]
print(list3)


# deleting the list by pop() method 
# the pop() is use to remove the last item .
# it works like first in last out


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
popped_motorcycle1=motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)
print(popped_motorcycle1.title())

#  unsure whether to use the del statement or the pop() method,
# here’s a simple way to decide: when you want to delete an item from a list
# and not use that item in any way, use the del statement; if you want to use an
# item as you remove it, use the pop() method


# you can remove it as a string also if we  dont know the value of it

wist = [ 'apple' , 'banana' , 'lichi']
wist.remove('apple')
print(wist)

# The remove() method deletes only the first occurrence of the value you specify. If there’s
# a possibility the value appears more than once in the list, you’ll need to use a loop
# to make sure all occurrences of the value are removed.