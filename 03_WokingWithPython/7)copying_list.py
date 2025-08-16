my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


# This doesn't work:
# u friend_foods = my_foods

# we set friend
# _foods equal to my_foods. This syntax actually tells Python to associate
# the new variable friend_foods with the list that is already associated with
# my_foods, so now both variables point to the same list. As a result, when we
# add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice
# cream' will appear in both lists, even though it appears to be added only to
# friend_foods.





my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)