# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
list= ['vito' , 'FCB' , 'extra' , 'punisher' , 'i am khan' , 'abrakadabra' , 'excallibur']
# •	 Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
print(f'The first three items in the lists are:-{list[:3]}')
# •	 Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
print(f'The middle elemetb of the list are :- {list[2:5]}')
# •	 Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.
print(f'The last three items in the list are :- {list[-3:]}')








# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:

pizzas= [ 'margrita', 'peperoni' , 'arvioli']
friend_pizzas = pizzas[:]
# •	 Add a new pizza to the original list.
pizzas.append('double_cheeze')
# •	 Add a different pizza to the list friend_pizzas.
friend_pizzas.append('choubble_deez')
# •	 Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
for pizza in pizzas:
    print(f'My favourite pizzas are')
    print(pizza)
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
for friend_pizza in friend_pizzas:
    print(f"My friends favourite pizzas are")
    print(friend_pizza)
# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.