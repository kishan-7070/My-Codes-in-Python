a=int(input("enter maths marks:"))
b=int(input("enter science marks:"))
c=int(input("enter sst marks:"))
d=int(input("enter coi marks:"))
e=int(input("enter computer marks:"))
def sum(e,f,g,h,i):
    total=e+f+g+h+i
    percent=(total/500)*100
    print("total marks:",total)
    print("%age:",percent)
    if(percent>90):
        print("grade A")
    elif(percent>80 and percent<=90):
        print("Grade B")
    elif(percent70 and percent<=80):
        print("Grade C")
    elif(percent>60 and percent<=70):
        print("Grade D")
    else:
        print("Grade E")
sum(a,b,c,d,e)










