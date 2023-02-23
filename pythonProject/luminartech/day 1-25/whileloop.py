#WHILE LOOP
#WHILE(CONDITION):
#BODY OF THE LOOP
'''


i=1
s=int(input("enter the limit"))
sum=0
while i<=s:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)
'''

#print didits
# n=int(input("enter the number"))
# num=n
# sum=0
# while n>0:
#     d=n%10
#     print(d)
#     n=n//10
#     sum=sum+d**3
# print("sumof digits:",sum)

#amstrong number
#are the num,ber that have sum of the cubes of the digits

'''
n=int(input("enter the number"))
num=n
sum=0
while n>0:
    d=n%10
    n=n//10
    sum=sum+d**3
if num==sum:
    print("amstrong")
else:
    print("not amstrong")
    '''

#AMTRONG NUMBER OF MULTIPLE DIGIT
n=int(input("enter a number to check"))
num1=num=n
sum=0
c=0
while n>0:
    n=n//10
    c=c+1
while num>0:
    d=num%10
    num=num//10
    sum=sum+d**c
if sum==num1:
    print("amstrong")
else:
    print("not amstrong")


