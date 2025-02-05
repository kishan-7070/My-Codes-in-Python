#How can we change element of a tuple
from functools import reduce
import math
'''''
x=(1,3,2,4,6,8,5,10)
list1=list(x)
list1[3]='19'
tuple1=list1
print(tuple1)
'''''
#Dictionary (Mutable,Ordered)
'''
x={"Name":"Anuj","Class":"7","Age":"38","home":"Noida"}
print(x)
print(type(x))
z=x.keys()
print(z)
y=x.values()
print(y)
'''
#Access Elements
'''
n=x.get("Age")
print(n)
'''
#Add elements with keys and values
'''
x["eligible"]='Yes'
print(x)
'''
#WAP to check a input is pallindrome or not
'''
n=input("Enter a input: ")
m=n[::-1]
if(m==n):
    print("pallindrome")
else:
    print("Not a pallindrome")
'''
#1+4+27+256+3125+.....
'''
n=int(input("Enter a number: "))
s=0
for i in range(1,n+1):
            s=s+i**i
print("Sum is: ",s)
'''
#Perfect number or not
'''
n=int(input("enter a number: "))
fac=[]
s=0
for i in range(1,n//2+1):
    if n%i==0:
        s+=i
        fac.append(i)
print("List of factors are: ",fac)
if(s==n):
    print("Perfect number")
else:
    print("Not a perfect number")
'''
#Print Prime numbers
'''
n=int(input("Enter a number: "))
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if(count==2):
        print(i)
'''
#Fibonacci Sequence
''''
n=int(input("Enter a number: "))
a=-1
b=1
c=0
while c<=n:
    c=a+b
    if c<=n:
        print(c)
    a=b
    b=c
'''
#Anagrams and Not Anagrams
'''
str1=input("Enter a string: ")
str2=input("Enter another string: ")
a=str1.lower()
b=str2.lower()
if sorted(a)==sorted(b):
    print("Anagrams")
else:
    print("Not a Anagrams")
'''
#Calculate Total number of vowels and consonants
'''
n=input("Enter a string: ")
h=n.lower()
count=0
k=0
for num in h:
    if num=="a" or num=="e" or num=="i" or num=="o" or num=="u" :
        count+=1
    else:
        k+=1
print("Consonant:",k)
print("Vowel:",count)
'''
#Anonymous Function(Inline Functions)
'''
x=[4,3,2,6,7,8,9]
add=reduce(lambda a,b:a+b,x)
print(add)
'''
#Largest no in the list
'''
x=[4,3,2,6,7,8,9]
largest=reduce(lambda a,b:a if a>b else b,x)
print(largest)                                                                                                                              
'''
#Square of each element in a list
'''
x=[4,3,2,6,7,8,9]
sq=list(map(lambda y:y**2,x))
print(sq)
'''
#Import Math Modules
'''
x=math.factorial(5)
print(x)
y=math.pow(5,2)
print(y)
'''
#String Mutable or Immutable ?
'''
x="Hello"
x[2]="S"
print(x)
// So String is Immutable
'''
#String Method(Shortcuts)
'''
x="hello"
y='python'
print(x.capitalize())
print(x.lower())
print(x.upper())
print(x.casefold())
print(x.swapcase())
print(x.count("l"))
print(x.replace('l','x'))
'''
#List Shortcuts
x=[1,2,3,2,3,4,5,6,2,1,3]
y=x.copy()
print(y)
print(y.count(2))
print(y.remove(3))













