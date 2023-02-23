#TUPLE ITS IS A UNCHANGABLE GROUP NOF HETROGENIOUS ELEMENT
#SO ITS CALLED IMMUTABLE
'''


tuple=(1,2,4,3,6,3,66,44,99,0)
newtup=()

#len()

print(len(tuple))

#min()
print(min(tuple))
print(max(tuple))

#index()

print(tuple.index(4))

#count()
print()
print(tuple.count(3))
'''


#tuple to list conversion
'''

tup=(2,4,1,6,8)
lst=list(tup)
print(lst)
'''

#create a new tuple contain even number only
'''

tup=(1,3,6,4,7,9,2,5)
tup2=[]
lst=list(tup)
for i in lst:
    if i%2==0:
        tup2.append(i)
tup3=tuple(tup2)
print(tup3)

'''

#finding max without using any function
'''

tup=(4,5,2,6,8)
max=0
for i in tup:
    if i>max:
        max=i
print(max)
'''

#inputing tuple

# tup=tuple(input("enter the elemt of the tuple").split())
# print(tup)

#FINDING THE COUNT OF ELEMENT GREATER THAN 10

tup=(11,33,5,7,222,55,8,0,4,)
c=0
for i in tup:
    if i>10:
        c=c+1
print(c)


