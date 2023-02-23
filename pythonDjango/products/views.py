from products.models import mobiles
# print(len(mobiles))
# print([mob.get("name") for mob in mobiles])
# print([mob.get("brand") for mob in mobiles])
# mobiles.sort(key=lambda m:m.get("price"),reverse=True)
# print(mobiles)

# costly_mobiles=max(mobiles,key=lambda m:m.get("price"))
# print(costly_mobiles)
# cheap=min(mobiles,key=lambda m:m.get("price"))
# print(cheap)
lst=[
    [10,11],
    [20,30],
    [40,50]
]
a=max([n for sublist in lst for n in sublist])
print(a)