# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.

simple_food = ('chicken lollipop' , 'banana fired' , 'chicken kaab' , 'anda rice' , 'bengal penis')

# •	 Use a for loop to print each food the restaurant offers.

for food in simple_food:
    print(food)

# •	 Try to modify one of the items, and make sure that Python rejects the
# change.

# simple_food[0]='bengali tiger'
# print(simple_food)

# •	 The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

simple_food = ('chicken lollipop' , 'banana fired' , 'chicken kaab' , 'anda bhurji' , 'chicken korma')
print("\nThe new modified menu is :- ")
for food in simple_food:
    print(food)