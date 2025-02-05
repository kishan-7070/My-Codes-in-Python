#Heron's Formula
x = int(input("Enter the value of  x "))
y = int(input("Enter the value of  y "))
z= int(input("Enter the value of z "))
s=(x+y+z)/2
a=s*(s-x)*(s-y) *(s-z)
Area = a**(1/2)

print("Area is : ",Area)