n=int(input("Enter a number: "))
fact=1
i=1
s=0
while i<=n:
    fact=fact*i
    s=s+fact
    i+=1
print(s)
