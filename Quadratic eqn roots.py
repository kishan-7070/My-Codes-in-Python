a=int(input("Enter 1st nu.: "))
b=int(input("Enter 2nd nu.: "))
c=int(input("Enter 3rd nu.: "))
m=(b**2-4*a*c)
h=m**(1/2)
s=(-b+h)/2*a
g=(-b-h)/2*a
if(h>0) :
    print("Roots are real and distinct")
    print("1st root is: ",s)
    print("2nd root is: ",g)
elif(h==0):
    print("roots are equal")
    print("equal root will be: ",s)
else:
    print("Imaginary root")
    
