n=[2,4,3,4]
def even(x):
    if x%2==0:
        return True
    else:
        return False
y=list(filter(even,n))
print(y)
