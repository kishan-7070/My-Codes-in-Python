n=int(input("enter a number: "))
def fact(a):
    fac=1
    for i in range(1,a+1):
        fac*=i
    print(f"factorial of {a} is:",fac)
fact(n)
