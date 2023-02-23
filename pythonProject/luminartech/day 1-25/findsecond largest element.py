#FIND THE SECOND LARGEST ELEMENT IN THE LIST
'''


list=[1,3,5,2,7.5,11,13,17,4]
list.sort()
print(list[-2])
print(list)
'''
#CREATE A NEW LIST THAT CONTAIN ONLY EVEN NUMBERS FROM EXISTING LIST
'''

list=[1,3,5,2,7.5,11,13,17,4]
newlist=[]
list2=[]
for i in list:
    if i%2==0:
        newlist.append(i)
    else:
        list2.append(i)
    #newlist=i
print("even",newlist)
print("odd",list2)

#print(list)
'''
'''
###INPUTING A LIST
list=input("enter the numbers").split(",")
print(list)

lst=input("enter the elemts").split()
list2=[]
list3=[]
for i in lst:
    if int(i)%2==0:
        list2.append(int(i))
    else:
        list3.append(int(i))
print(list2)
print(list3)

'''
"""

#REMOVING DUPLICATE ELEMTS FROM LIST(h/w)
list=input("emter the elents").split()
list2=[]
for i in list:
    if int(i) not in list2:
        list2.append(int(i))
print(list2)

"""
'''

lst=['a','apple','App','banu','Ahmed','Banana','Apple']
print(lst.count('apple'))
print(lst.index('banu'))

#POP  deleting element using index number
lst.pop(3)
print(lst)

#REmove deleting using the item name
lst.remove('App')
print(lst)

'''
'''
#MAKING THE LIST TO UPPER CASE
lst=['cat','dog','cow','goat']
newlst=[]
for i in lst:
   x=i.upper()
   newlst.append(x)
print(newlst)


'''
#NESTED LIST
lst=[1,3,4,[55,77,[11,44],77],22,88]
print(lst[3][2][1])
print(lst[3][3])