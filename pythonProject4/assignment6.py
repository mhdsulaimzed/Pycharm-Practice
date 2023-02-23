#last digit is divisible by 4

num=int(input("enter the number"))
if (num%10)%4==0:
    print("divisible")
else:
    print("not divible")