#checking prime
num=int(input("enter the number to check"))
c=0
for i in range(1,num+1,1):
    if num%i==0:
        c=c+1
if c==2:
    print("its prime number")
else:
    print("its not a prime number")
