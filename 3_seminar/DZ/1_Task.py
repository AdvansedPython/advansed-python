friends = {"Lee":("bag","laptop", "axe","tent","shoes","clothes"),\
           "Jerry":("clothes","sleeping bag","burner","water","meal","lantern","first aid kit"),\
            "Rick":("tent","shoes","clothes","water","meal","lantern")}

all_items = []
items_all_friends = None
item_one_friend = dict()
items_all_friends = None

for key, value in friends.items():

    # есть у всех
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
            staff = "Печально, но нет уникальности("
        item_one_friend[key] = staff

    # Есть у всех кроме одного
    
        
            

print(f"Уникальные предметы: \n{item_one_friend}\n")
    
print(f"Предметы, которые есть у всех: \n{items_all_friends}")
