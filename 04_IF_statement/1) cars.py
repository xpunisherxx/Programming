cars = ['audi' , 'bmw' , 'subaru' , 'supra']

for car in cars:
    if car== 'bmw':
        print(car.upper())
    else:
        print(car.title())


# inequality is dont by !=

# checking whetere the item is in the list or not 

banned_users = ['andrew' , 'carolina' , 'david']
user = input("enter your name bch as")

if user not in banned_users:
    print(f'{user.title()} , you can posed the response if you wish')

    