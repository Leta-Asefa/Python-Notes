file=open('file.txt','r')

# print(file.read())  # prints all lines
# print(file.readline(),end="")
# print(file.readline())

line=file.readline()

while line!='':             #file.readLine() returns '' (empty string) while it reacs the end of line
    print(line,end="")
    line=file.readline()









