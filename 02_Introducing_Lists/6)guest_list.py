# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

list= [ 'swittie fox' , 'cory chase' , 'elezabeth olzen']

print(f'whould you like to go to dinner {list[0]}')
print(f'whould you like to go to dinner {list[1]}')
print(f'whould you like to go to dinner {list[2]}')



# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.

# •	 Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.

print(
    f' snitches {list[0]} , {list[1]}'
)

# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.

print('therefore the new good members are :- ')
list[0] = 'Mia Khalifa'
list[1]= 'torry Daniels'
print(f'The Real Stars {list}')
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.

print(f'yo! {list[2]} wanna smash bae !!')



# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
list.insert( 0 , 'Mao Hamasaki')
# •	 Use insert() to add one new guest to the middle of your list.
list.insert( 3 , 'scarlet jonson')
# •	 Use append() to add one new guest to the end of your list.
list.append('skyler Vox')
# •	 Print a new set of invitation messages, one for each person in your list.
# waste of time i wont do it 
print(list)