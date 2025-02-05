n=int(input("Enter a number: "))
t=n
s=0
count=0
while t>0:
    t//=10
    count+=1
print("Count is:",count)
i=count
t=n
while t>0:
    a=t%10
    s=s+a**i
    i=i-1
    t//=10
print("Sum is: ",s)
if(s==n):
    print("Disarium number")
else:
    print("Not Disarium number")
