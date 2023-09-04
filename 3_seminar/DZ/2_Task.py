my_lst = [1,1,2,2,3,4,5,6,None, None, 5]
my_set = set(my_lst)
result = []

for item in my_set:
    if my_lst.count(item)>1:
        result.append(item)

print(result)