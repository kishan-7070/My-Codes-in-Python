a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
print("Welcome to Arithmetic Calculator :")
print("Select option:")
print("1.Addition(+)")
print("2.Substraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
x=int(input("Enter options to exexute: "))
if(x==1):
    print(f"Addition of {a} and {b} is:",a+b)
elif(x==2):
     print(f"Substraction of {a} and {b} is:",a-b)
elif(x==3):
 print(f"Multiplication of {a} and {b} is:",a*b)
elif(x==4):
     print(f"Division of {a} and {b} is:",a/b)
