n1=int(input("Enter time1 hours: "))
n2=int(input("Enter time1 minutes: "))
n3=int(input("Enter time2 hours: "))
n4=int(input("Enter time2 minutes: "))
t=n1+n3
m=n2+n4
if(m<60):
    print(f"Total time is {t} hours and {m} minutes")
elif(m>=60):
    m=m-60
    t=t+1
    print(f"Total time {t} hours and {m}minutes")
