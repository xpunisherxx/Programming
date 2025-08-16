# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

# def shirt(size_s , print_s):
#     print(f"the size of the shirt is {size_s} and the meesage printed on it is {print_s}")

# size_s1 = int(input("enter the size u need"))
# print_s1 = input("enter the printing on the Ts")

# shirt(size_s=size_s1 , print_s=print_s1)

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

# def shirt(print_s, size_s="LARGE"):
#     print(f"The size of the shirt is {size_s} and the message printed on it is '{print_s}'.")

# size_s1 = input("Enter the size you need: ")
# print_s1 = input("Enter the printing on the T-shirt: ")

# # If the user doesn't enter size, use default
# if size_s1.strip() == "":
#     shirt(print_s1)
# else:

#     shirt(print_s1, size_s1)


# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country

def city(city , country ="Iceland"):
    print("{city} is in {country}")

