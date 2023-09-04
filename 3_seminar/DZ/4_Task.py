from pprint import pp

things = {"bag":15,"laptop":2, "axe":2,"tent":5,"shoes":1,"clothes":2,"sleeping bag":5,"burner":1, \
          "water":3,"meal":4,"lantern":1,"first aid kit":2}

bag = {}
bag_tonnage = things.pop("bag")
variants = []


for key,value in things.items():
    
    if len(bag) == 0 or sum(bag.values())+value < bag_tonnage:
            bag[key] = value
        
        
if bag not in variants:
    variants.append(bag)
        


pp(variants)
