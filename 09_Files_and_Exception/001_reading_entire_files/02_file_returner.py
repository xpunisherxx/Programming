with open('/home/ex/practice_python/09_Files_and_Exception/001_reading_entire_files/01_pi_digit.txt') as file_object:
# the open funciton dosent take ~ = home/ex... coz this stuff is not valid 
# as object_file is Alias
# Opne to access the file

# You could open
# and close the file by calling open() and close(), but if a bug in your program
# prevents the close() method from being executed, the file may never
# close.
    contents = file_object.read()


# The only difference between this output and the original file is the
# extra blank line at the end of the output. The blank line appears because
# read() returns an empty string when it reaches the end of the file; this empty
# string shows up as a blank line. If you want to remove the extra blank line,
# you can use rstrip() in the call to print():

print(contents)
print(contents.rstrip())
