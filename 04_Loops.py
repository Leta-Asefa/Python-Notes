counter=0
while counter<5:
    print('Python For You : '+ str(counter))
    counter+=1


i=0
while i<5:
    print("Welcome to Python ",end="")
    j=0
    while j<4:
        print(str(j)+" ",end="")
        j+=1
    print()
    i+=1


#----------------------for Loop------------------

list=['a','b','c','d','e']
for i in list:
    print(i)
for i in range(10,1,-2):
    print(i)
#--------------------break -------continue ----------pass -----

for i in range(1,101):
    if(i==5):
        print("break")
        break
    else: print(i)
    i+=1


for i in range(1,20):
    if(i==5 or i==3):
        print("continue")
        continue
    else: print(i)
    i+=1

for i in range(90,100):
    if(i==93):
        pass #means just ignore this block
    else: print(i)
    i+=1

























