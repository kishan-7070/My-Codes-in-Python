n=int(input("Enter a number: "))
s=0
while n>0:
      a=n%10
      s+=a
      n//=10
print(s)
