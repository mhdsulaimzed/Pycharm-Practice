tup=(1,3,5,6,7,9,3,5)
lst2=[]
for i in tup:
    if i%3==0:
        lst2.append(i)
tup3=tuple(lst2)
print(tup3)