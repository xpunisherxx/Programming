# list = ['charles' ,'orange' , 'black_panther' , 'white_tiger' , 'iron_fist' , 'nigasaurus']
# print(list[0:3])

# print(list[:4])

# print(list[2:])

# print(list[-3:])    #the list is also going in reverse order

players= ['spider_man' , "iron_fist" , 'agnet_venom' , 'wanda' , 'scarlet_spider' , 'dare_devil']
print("Here are the number of players that are selected in the sport section")

for player in players[:3:]:
    print(player.title())
