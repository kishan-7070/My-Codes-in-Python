#Area of circle 
#Area of  rectangle
#Area of square
r = int(input("Enter the value of radius : "))
l = int(input("Enter the value of length : "))
b = int(input("Enter the value of breadth : "))
s = int(input("Enter the value of Side : "))
h = int(input("Enter the value of height : "))
Vol_cyl=3.14*r*r*h
Vol_sph= (4/3)*3.14*r*r*r
Vol_cone=(1/3)*3.14*r*r*h
Area_Circle = 3.14*r*r
Circm = 2*3.14*r
Area_rect = l*b
Area_sq = s*s
per_rect = 2*(l+b)
print("Volume of Cylinder is : ",Vol_cyl)
print("Volume of sphere is : ",Vol_sph)
print("Volume of Cone is : ",Vol_cone)
print("Area of circle is : ",Area_Circle)
print("Circumference  of circle is : ",Circm)
print("Area of rectangle is : ",Area_rect)
print("Perimeter of rectangle is : ",per_rect)
print("Area of Square is : ",Area_sq)