# with open('/home/ex/practice_python/09_Files_and_Exception/002_Reading_line_by_line/02_pi_file.txt') as file_object:
#     for lines in file_object:
#         print(lines)


# OR WE COULD DO IT LIKE :-


filename = '/home/ex/practice_python/09_Files_and_Exception/002_Reading_line_by_line/02_pi_file.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())