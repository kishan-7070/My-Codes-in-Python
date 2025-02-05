#Swap two numbeers without using 3rd variable
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print("Before swapping ({},{}) ".format(a,b))
a=a+b
b=a-b
a=a-b
print("After swapping ({},{}) ".format(a,b))
