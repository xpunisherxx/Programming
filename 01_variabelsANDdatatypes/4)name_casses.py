# 2-3. Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?


fname = 'hello rahul upadhyay'
sname=" , would you like to learn python today ?"
cap_fname = fname.title()

print(f"{cap_fname}{sname}")

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.

n_name = 'rahul upadhyay'

print(n_name.lower())
print(n_name.upper())
print(n_name.title())


# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new.”


quote = '"kal kare so aaj kar aaj kare so abhi... age ka nhi ata"'
name_author = "satyam charles mahammad motokhevyakha"

print(f"{name_author} once said, {quote} ")









# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
# famous person’s name using a variable called famous_person. Then compose
# your message and represent it with a new variable called message. Print your
# message.


quote = '"kal kare so aaj kar aaj kare so abhi... age ka nhi ata"'
name_author = "satyam charles mahammad motokhevyakha"
famous_person  = "heral of foul blodded arcane"

print(f"{name_author} once said, {quote} ")
print(f"{famous_person} once said, {quote} ")