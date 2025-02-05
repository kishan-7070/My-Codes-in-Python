f=open(r"C:\Users\kisha\OneDrive\Desktop\Txt file  handling\1.txt","r")
c=f.read()
f.close()
f1=open(r"C:\Users\kisha\OneDrive\Desktop\Txt file  handling\2.txt","r")
d=f1.read()
f1.close
e = c+d
f2=open(r"C:\Users\kisha\OneDrive\Desktop\Txt file  handling\1+2=3.txt","a")
f2.write(e)
f2.close()
f3 =open(r"C:\Users\kisha\OneDrive\Desktop\Txt file  handling\1+2=3.txt","r")
print(f3.read())

