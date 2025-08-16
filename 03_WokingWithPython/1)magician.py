# simple looping 

magicians = ['alice' , 'david' , 'estrogen']
for magician in magicians:
    print(f'good trick , {magician.title()}')

# here’s a good way to
# start a for loop for a list of cats, a list of dogs, and a general list of items:
#     for cat in cats:
# for dog in dogs:
# for item in list_of_items:



# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.

# •	 Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
pizzas = ['margerita' , 'peperoni' , 'hawaiin']
for pizza in pizzas:
    print(f'i line {pizza} pizza')
# •	 Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
print("i really pizza ! \ni rally like pizza coz i really like them \nI really love pizza!!")


# execution of the range funciton

for value in range(1,5):
    print(value)

# we can convert the range function in list  and we can also skip numebrs
number = list(range(1,6,2))
print(number)


