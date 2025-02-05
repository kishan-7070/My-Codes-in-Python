str1=input("enter a string: ")
str2=input("enter another string: ")
def string(a,b):
    m=a.lower()
    n=b.lower()
    if(sorted(m)==sorted(n)):
        print("Anagrams")
    else:
        print("Not Anagrams")
string(str1,str2)
