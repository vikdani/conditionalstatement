# enter details of vehicle, if average is greater than 60 than find out cost of journey adn print all the details
vn=input("enter vehicle name")
vp=int(input("enter vehicle price"))
vkm=int(input("enter running kilometre of vehicle"))
va=int(input("enter average of vehicle"))
vpp=int(input("enter 1 litre petrol price "))
litreconsumed=vkm/va
totalcost=litreconsumed*vpp 
if (va>60):
    print("vehicle name",vn)
    print("vehicle price",vp)
    print("vehicle average",va)
    print("vehicle running km",vkm)
    print("litre consumed in journey",litreconsumed)
    print("total cost of journey",totalcost)    







