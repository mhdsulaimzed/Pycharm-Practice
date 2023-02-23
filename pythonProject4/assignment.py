#vote check
print("VOTE ELIGBLITY CHECKER")
age=int(input("enter the age of person"))
if age>18:
    print("Eligible")
else:
    print("Underage")

#TO CHCK WHETHER THE NUMBER IS DIVIDBLE BY NUMBER 7

num=int(input("enter a number"))
if num%7==0:
    print("divisible")
else:
    print("not divisble")

#odd or even
num=int(input("ente  a number"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")


#divisble by 5 hello and bye
num=int(input("enter a number"))
if num%5==0:
    print("hello world")
else:
    print("Bye")

#electricity bill
unit=int(input("enter the units"))
if unit<100:
    print("no cost")
elif unit>=100 and unit<200:
    s=5
    print(unit*5)
elif unit>200:
    s=10
    print(unit*10)

#last digit is divisible by 4

num=int(input("enter the number"))
if (num%10)%4==0:
    print("divisible")
else:
    print("not divible")

# mark pecentage to rade
mark=int(input("enter the mark"))
if mark>90:
    print("A")
elif mark>80 and mark<=90:
    print("B")

elif mark>=60 and mark<=80:
    print("C")

# road tax for vehicle
price=int(input("enter the vehicle price"))
if price>100000:

    print((price/100)*15)
elif price <=100000 and price>50000:
    print((price / 100) * 10)

elif price<50000:
    print((price / 100) * 5)

year=int(input("enetr the year"))
if year%4==0:
    print("leap")
else:
    print("not a leap")

#day with number
i=int(input("eneter number btw 1 and 7"))
list1=["null","sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
print(list1[i])