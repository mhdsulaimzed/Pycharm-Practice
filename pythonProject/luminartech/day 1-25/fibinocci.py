#fibanacci
'''num=int(input("enter the limit"))
f=0
s=1
for i in range(1,num+1):
    print(f,end=" ")
    t=f+s
    f=s
    s=t
'''
#for loop in secuence
# body of the loop
'''
s=input("enter the string")
for i in s:
    print(i)
'''
#counting string leangth
'''
s=input("entr the strng")
c=0
for i in s:
    c=c+1
print(c)
'''
#vowels checking
'''
s=input("Enter the string")
v=0
for i in s:
    if i in 'aeiouAEIOU':
        v=v+1
print("count of vovwl:",v)
'''
#ADDING TWO NUMBERS
'''
a=int (input("enter two numbers"))
b=int (input())
c=int (input())
avg=a+b+c
print(avg/3)
'''
#COUNTING VOWELS SPACES AND CONSONANTS
'''

s=input("enter the string")
v=0
sp=0
c=0
for i in s:
    if i in 'aeiouAEIOU':
        v=v+1
    elif i in " " :
        sp=sp+1
    else:
        c=c+1
print("vowels",v,"spaces",sp,"consonents",c)
'''
