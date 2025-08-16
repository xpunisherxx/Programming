# alien_0= {'color' : 'green' , 'speed' : 'slow'}
# print(alien_0['points'])

# we'll get error with this 
# BUT
# heres how we deal with this error
alien_0= {'color' : 'green' , 'speed' : 'slow'}
point_value = alien_0.get('points' , 'No value assinged. ')
print(point_value)


# If you leave out the second argument in the call to get() and the key doesn’t exist,
# Python will return the value None. The special value None means “no value exists.”
# This is not an error: it’s a special value meant to indicate the absence of a value.

