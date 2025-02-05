#Exception Handling
a=int(input("Enter a number: "))
b=int(input("Enter 2nd number: "))
try:
    x=a/b
    print(x)
except ZeroDivisionError:
    print("Not a Valid number")
except ValueError:
    print("Not a valid int")#Agr koi input int ke jgh char de de to
finally:
    print("Yes")
    #We can use raise , finally and else statement
