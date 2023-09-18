#enter two no., if second is greater than first than swap the number 

a=int(input("enter first number"))
b=int(input("enter second number"))
if(b>a):
    c=a
    a=b
    b=c
    
    print("after swapping ",a,b)
