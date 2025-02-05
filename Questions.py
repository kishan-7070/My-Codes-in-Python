          # CUBE Print in a list
''''
x=[]
for i in range(11):
    x.append(i**3)
print(x)
          #List Comprehension
y=[i**3 for i in range(11)]
print(y)
'''''
           #WAP to print table of x using list comprehension
x=int(input("Enter a number: "))
print([x*i for i in range(1,11)])

