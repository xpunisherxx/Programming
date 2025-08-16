# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.



# inside_text ="Hello , Sir/Ma'am welcome to Dominoze !!"
# inside_text+= "\nwhat would you like to order?"
# toppings = []
# while True:
#     prompt = input(inside_text)
#     print(prompt)
#     if prompt == 'quit':
#         print("Thanks , your order has been placed , please visit again")
#         break
#     else:
#         toppings.append(prompt)
#     print(toppings)

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

while True:
    age_input = input("Enter your age (or type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        print("Goodbye!")
        break

    # Convert input to number after checking 'quit'
    user_age = int(age_input)

    if user_age < 3:
        print("Congratulations, your ticket is FREE!")
    elif 3 <= user_age <= 12:
        print("Your ticket costs $10.")
    else:
        print("The cost of your ticket is $15.")

         


