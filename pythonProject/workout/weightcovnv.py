w=float(input("enter the wieght"))
d=input("wieght is in K for kilo and L for pound")
if d=="k" or "K":
    p=w*0.45
    print("weight in lbs:"+str(p)
elif d=="L" or "l":
    k=w/0.45
    print("weight in kilo"+str(k)
else:
    print("enter only K or L")