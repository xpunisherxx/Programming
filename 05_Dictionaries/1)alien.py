# alien_0 = {'color' : 'green' , 'point' : 5 }

# print(alien_0['color'])
# print(alien_0['point'])

# # dictionaries can kay and valie pairs in them ....

# # A key’s value can be a number, a string, a list, or even another dictionary.

# # adding a new value
# alien_0 ['x-coordinate'] = 0
# alien_0['y-coodinate'] = 25
# print(alien_0)

# starting with an empty dictionary
# 


#

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# removing the key value pair

del alien_0['y_position']
print(alien_0)