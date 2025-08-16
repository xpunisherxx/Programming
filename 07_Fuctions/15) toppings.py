def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom' , 'green peppers' , 'exxtra cheese')
# * the star tells the python function to make a tuple called toppings, containing all the values this 
# functions recieves

# In Python, arbitrary arguments (also called variable-length arguments) 
# let you pass an unknown number of values into a function. You’ll see these with *args and **kwargs

