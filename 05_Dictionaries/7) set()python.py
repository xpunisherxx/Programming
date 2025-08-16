# When you wrap set() around a list that contains duplicate items, Python
# identifies the unique items in the list and builds a set from those items. At u
# we use set() to pull out the unique languages in favorite_languages.values().


# set() does not "randomly" pull out values. It simply removes duplicates and stores unique elements.

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())