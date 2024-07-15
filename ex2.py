cost=100
quantity=int(input("enter quantity"))
totalcost=cost*quantity
if totalcost>1000:
    discount=totalcost*(10/100)
    price=totalcost-discount
    print("After discount the price is",price)
else:
    print("the price is ",totalcost)    