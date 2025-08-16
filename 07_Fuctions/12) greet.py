def greet_user(names):
    for name in names:
        print(f"hello {name.title()}")
    
usernames = ['hannah' , 'alice' , 'nija']
greet_user(usernames)