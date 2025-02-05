from functools import reduce
''''
#WAP to check whether two strings are  anagrams or not
a=input("Enter 1st string:" )
b=input("Enter 2nd string:" )
x=a.lower()
y=b.lower()
if(sorted(x)==sorted(y)):
    print("These are Anagrams")
else:
    print("These are not Anagrams")
'''''
'''''
#WAP  to count the vowels in a string
n=input("Enter a string : ")
a=len(n)
count =0
for i in range(0,a):
    if(n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u'):
       count+=1
print("Total number of vowel in the string is:",count)
'''''
'''''
#WAP to print fibbonacci sequence
n=int(input("Enter a number:"))
def fib(a):
    if(a==0):
        return 0
    elif(a==1):
        return 1
    else:
        return fib(a-1)+fib(a-2)
for i in range(0,n):
    print(fib(i),end=" ")
'''''
'''''
#WAP to print factorial using recursion
n=int(input("Enter a number: "))
def fact(a):
    if(a==0):
        return 1
    elif(a==1):
        return 1
    else:
        return a*fact(a-1)
print(f"Factorial of {n} is :",fact(n))
'''''
'''''
#WAP to print the square of two given number
n=int(input("Enter a number: "))
add=lambda x:x**2
print(add(n))
'''''
'''''
#WAP to check a number is ODD or EVEN
n=int(input("Enter a number: "))
even=lambda x:"EVEN"if(x%2==0) else "ODD" if(x%2!=0) else "Not a number"
print(even(n))
'''''
'''''
#WAP to square every element in the list
x=[23,4,66,2,4,6,8,9,7,5]
def sq(n):
    return n**2
a=list(map(sq,x))
print("After squarring elements are:",a)
'''''
'''''
#From another method
x=[23,4,66,2,4,6,8,9,7,5]
a=list(map(lambda n:n**2,x))
print("After Squarring :",a)
'''''
'''''
#WAP to make a list of even number
x=[23,4,66,2,4,6,8,9,7,5]
'''''
'''''
def even(n):
    if(n%2==0):
        return True
    else:
        return False
a=list(filter(even,x))
print(a)
'''''
'''''
a=list(filter(lambda n:True if(n%2==0) else False,x))
print("Even numbered list:",a)
'''''
'''''
#WAP to sum of all numbers in the list
x=[23,4,66,2,4,6,8,9,7,5]
a=reduce(lambda m,n:m+n,x)
print(a)
'''''





















    
