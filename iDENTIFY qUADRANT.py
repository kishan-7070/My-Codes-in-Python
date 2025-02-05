x=int(input("Enter 1st coord:: "))
y=int(input("Enter 2nd coord: "))
if(x>=0 and y>=0):
    print("both x and y are in 1st quadrant")
elif(x>=0 and y<=0):
    print("both x and y are in 4th quadrant")
elif(x<=0 and y>=0):
    print("both x and y are in 2nd quadrant")
else:
    print("both x and y are in 3rd quadrant")
