
# When writing a function, you can define a default value for each parameter.
# If an argument for a parameter is provided in the function call, Python uses
# the argument value. If not, it uses the parameter’s default value. So when
# you define a default value for a parameter, you can exclude the corresponding argument you’d usually write in the function call. Using default values
# can simplify your function calls and clarify the ways in which your functions
# are typically used.


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')










# When you use default values,
#  any parameter with a default value needs to be listed
# after all the parameters that don’t have default values.
# This allows Python to continue interpreting positional arguments correctly