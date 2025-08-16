# t ry i t yourse l F


# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:

# "Santiago, Chile"



# def city_country(city, country):
#     """Return a neatly formatted city and country."""
#     return f"{city}, {country}"

# # 👇 Get input from the user
# city_input = input("Enter the name of your city: ")
# country_input = input("Enter the name of your country: ")

# # 👇 Call the function with the inputs
# result = city_country(city_input, country_input)

# # 👇 Print the result
# print(result)


# Call your function with at least three city-country pairs, and print the
# values that are returned.






# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.



# def make_album(artist_name, album_title, num_songs=None):
#     album = {
#         'artist': artist_name,
#         'title': album_title
#     }
#     if num_songs:
#         album['songs'] = num_songs
#     return album

# # Making 3 albums
# album1 = make_album("Linkin Park", "Hybrid Theory")
# album2 = make_album("Eminem", "The Eminem Show", 20)
# album3 = make_album("Arijit Singh", "Soulful Vibes")

# # Print albums
# print(album1)
# print(album2)
# print(album3)


# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.










# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop...