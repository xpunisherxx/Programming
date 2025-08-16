name = 'rahul upadhyay'
print(name.title())
print(name.upper())

sname ='RAHUL UPADHYAY'
print(sname.lower())


# These strings are called f-strings. The f is for format, because Python
# formats the string by replacing the name of any variable in braces with its
# value.

print(f"{name} | {sname}")



# if we use python before 2.5 then we have to use f rahte than format
# full_name = "{} {}".format(first_name, last_name)



# /t = tab 
# /n = new_line 



# Python can look for extra whitespace on the right and left sides of a
# string. To ensure that no whitespace exists at the right end of a string, use
# the rstrip() method.

favourite_language = 'python '
favourite_language2= ' python'

print(favourite_language.rstrip())
print(favourite_language2.rstrip())