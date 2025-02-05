n=int(input("Enter a number: "))
d=n
s=0
while d>0:
      a=d%10
      s=s*10+a
      d//=10
print(s)
if(n==s):
    print("pallindrome")
else:
    print("Not a pallindrome")
