# Creating the Dog Class
# Each instance created from the Dog class will store a name and an age, and
# # we’ll give each dog the ability to sit() and roll_over():


class Dog:
    """A simple attempt to model a dog."""
# default constructors = jab sirf self ho. aur python would create that automatically
# parametarized deconstructor = python wont create. and identity = user
#  made extra function 
    def __init__(self, name, age):
        """Initialize name and age attributes."""

        self.name = name
        self.age = age
        pass

    def sit(self):
        """Simulate a dog sitting in reposne to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over")

command= Dog("jimmy good boi" , 5)
print(command.name)

print(command.age)

        