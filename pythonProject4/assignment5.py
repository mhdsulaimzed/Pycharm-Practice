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

