
a=(input("Enter 1st number: "))
if(a>='A' and a<='Z'):
    x=a.lower()
    print(f"Small alphabet of {a} is:",x)
elif(a>='a' and a<='z'):
    y=a.upper()
    print(f"Capital alphabet of{a} is:",y)
else:
    print("Not a alphabet")