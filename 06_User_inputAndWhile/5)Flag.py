# Key Points

#     Flags are typically named like active, found, finished, error, valid, etc.

#     The flag is often a True or False value.

#     You use it in loops, conditions, or event control.

# 🧠 Why Use a Flag?

#     To control the flow of a loop or function.

#     To mark whether a condition has occurred (like: "was an error found?").

#     To make code easier to understand and manage.


# In Python, a flag is just a variable (usually a Boolean) 
# used to signal when a condition has been met or a certain event
# has occurred during program execution.


active = True  # This is the flag

while active:
    message = input("Enter something (or 'quit' to stop): ")

    if message == 'quit':
        active = False  # Turn the flag off
    else:
        print(f"You said: {message}")


