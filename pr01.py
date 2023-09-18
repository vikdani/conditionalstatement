# input employee name, age, qualification and working experience . if working experience is greater than three year than print all the  details.

nm=input("enter name")
na=int(input("enter age"))
nq=input("enter qualification")
ne=int(input("enter working experience"))

if(ne>3):
    print("the name is",nm)
    print("the age is",na)
    print("the qualification  is",nq)
    print("the working experience  is",ne)