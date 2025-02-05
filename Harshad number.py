n=int(input("Enter a number: "))
t=n
s=0
while t>0:
    a=t%10
    s=s+a
    t//=10
print("Sum is: ",s)
if(s%6==0):
    print("Harshad number")
else:
    print("Not a harshad number")