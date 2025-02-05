n=int(input("Enter a number: "))
d=n
s=0
while d>0:
      a=d%10
      s=s+a*a*a
      d//=10
print(s)
if(s==n):
    print("Armstrong number")
else:
    print("Not a armstromg number")