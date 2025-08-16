# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name.capitalize()}!")


# with use of int 

prompt = "What was your age, Gary?!"
prompt += "\nHuh!!?? What was it again?\n"

age_input = input(prompt)

if not age_input.isdigit():
    print("You are not him lil bro.")
else:
    age = int(age_input)
    print(f"Your age is: {age}")
