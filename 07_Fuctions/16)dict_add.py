# the **user_info creates an empty dict . and take whatever name and value it recueves

def build_profile(first, last, **user_info):
    """Build the dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info 

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


# n o t e You’ll often see the parameter name **kwargs used to collect non-specific keyword
# arguments.