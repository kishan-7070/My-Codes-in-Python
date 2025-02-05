from functools import reduce
x=[23,32,43,12,27,76,45,68,95,87,16]
#print square of each element in the list
square=(list(map(lambda a:a**2 ,x)))
print(square)
#print only even after square
even = (list(filter(lambda a: True if a%2==0  else False,square)))
print(even)
#print even number in the list
even=(list(filter(lambda a:True if(a%2==0) else False,x)))
print(even)
#print sum of every element in x 
sum=reduce(lambda a,b:a+b ,x)
print(sum)
#All Odd numbers in the list
def odd(n):
    if n%2!=0:
        return True
    else:
        return False
m=list(filter(odd,x))
print(m)
#squares of all odd numbers
p=(list(map(lambda a:a**2,m)))
print(p)
#sum of squares of all odd  numbers
n=reduce(lambda a,b:a+b,p)
print(n)
