# When you call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to
# do this is based on the order of the arguments provided. Values matched
# up this way are called positional arguments.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')

# Order Matters in Positional Arguments



# Keyword Arguments
# A keyword argument is a name-value pair that you pass to a function. You
# directly associate the name and the value within the argument, so when you
# pass the argument to the function, there’s no confusion (you won’t end up
# 134 Chapter 8
# with a harry named Hamster). Keyword arguments free you from having
# to worry about correctly ordering your arguments in the function call, and
# they clarify the role of each value in the function call.




# The order of keyword arguments doesn’t matter because Python
# knows where each value should go. The following two function calls are
# equivalent:
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')