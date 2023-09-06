friends = {"Lee":("bag","laptop", "axe","tent","shoes","clothes"),\
           "Jerry":("clothes","sleeping bag","burner","water","meal","lantern","first aid kit"),\
            "Rick":("tent","shoes","clothes","water","meal","lantern")}

all_items = []
items_all_friends = None
item_one_friend = dict()
items_one_friend_dont_have = {}

# есть у всех
for key, value in friends.items():

    if items_all_friends == None:
        items_all_friends = value
    else:
        items_all_friends = set(items_all_friends) & set(value)


# есть только у одного
for key, value in friends.items():
    staff = []

    for key_friend, value_friend in friends.items():
        if key != key_friend:
            if staff == []:
                staff = set(value) - set(value_friend)
            else:
                staff = set(staff) - set(value_friend)

    if staff == set():
        continue
    item_one_friend[key] = staff

# Есть у всех кроме одного
# count_friends = len(friends)

# for key, value in friends.items():
#     for item in set(value):
#         all_items.append(item)
# for item in all_items:
    
# print(all_items)
        
            

print(f"Уникальные предметы: \n{item_one_friend}\n")
    
print(f"Предметы, которые есть у всех: \n{items_all_friends}")
