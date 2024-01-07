
#since python is dynamically typed , we can not apply overloading directly , so we'll use some trick

def sum(a=None,b=None,c=None):
    if(a!=None and b!=None and c!=None):
        return a+b+c
    elif (a!=None and b!=None):
        return a+b
    else :
        return a



print(sum(5))
print(sum(5,5))
print(sum(5,5,5))

#overriding -> first find in the child class, if it is there override the parent class' method , else call the parent's

