# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.

# •	 Store the locations in a list. Make sure the list is not in alphabetical order.

locations = ['nanital' , 'chandigarh' , 'dalhousi' , 'arunachal Pradesh']

# •	 Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.

print(locations)

# •	 Use sorted() to print your list in alphabetical order without modifying the
# actual list.

print(sorted(locations))

# •	 Show that your list is still in its original order by printing it.

print(locations)

# •	 Use sorted() to print your list in reverse alphabetical order without changing the
#  order of the original list.

print(sorted(locations , reverse=True))

# •	 Show that your list is still in its original order by printing it again.

print(locations)

# •	 Use reverse() to change the order of your list. Print the list to show
#  that its
# order has changed.

locations.sort(reverse=True)
print(locations)
# •	 Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.

print(locations)

# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.

locations.sort()
print(locations)

# •	 Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

locations.sort(reverse=True)
print(locations)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.

Guests = ['liza' , 'pizza' , 'cheeza' , 'rizza']
print(f"this is the number of guests that will arrive at the even :- {len(locations)}")

