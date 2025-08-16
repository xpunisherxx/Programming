# T ry I T yourse l f

# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes 
# individually, and then call both methods.



# class restraunt:
#     def __init__(self , restraunt_name , cuisine_type):
#         self.restraunt_name = restraunt_name
#         self.cuisine_type = cuisine_type
#         pass

#     def open_restraunt(self):
#         print(f"the {self.restraunt_name} is open now")

#     def close_restraunt(self):
#         print(f"the {self.cuisine_type} restraunt is not available Now!!")

# kitchen = restraunt("FiveGuys" , "burger")
# print(kitchen.restraunt_name)
# print(kitchen.cuisine_type)
# kitchen.open_restraunt()
# kitchen.close_restraunt()



# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.



# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is now open!")


# # Creating 3 instances
# restaurant1 = Restaurant("Tandoori Flames", "Indian")
# restaurant2 = Restaurant("Sushi Zen", "Japanese")
# restaurant3 = Restaurant("La Pizzeria", "Italian")

# # Calling describe_restaurant() for each instance
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()



# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user


class User:
    def __init__(self , first_name , last_name):
        self.first_name = first_name
        self.last_name = last_name
        pass

    def describe_user(self):
        print(f"the name of the user is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello! Welcome to the Show BAYBAY !! {self.first_name} ")


users = User("Rahul" , "Upadhyay")
print(users.first_name)
print(users.last_name)
users.greet_user()
users.describe_user()
