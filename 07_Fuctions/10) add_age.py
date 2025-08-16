def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

# person['age'] = age
# That's not appending — it's direct assignment, which means:
 # If the key 'age' doesn't exist → it adds it.
# If it already exists → it updates it.


musician = build_person('jimi', 'hendrix', age=27)
print(musician)