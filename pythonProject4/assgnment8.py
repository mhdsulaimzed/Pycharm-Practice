# road tax for vehicle
price=int(input("enter the vehicle price"))
if price>100000:

    print((price/100)*15)
elif price <=100000 and price>50000:
    print((price / 100) * 10)

elif price<50000:
    print((price / 100) * 5)