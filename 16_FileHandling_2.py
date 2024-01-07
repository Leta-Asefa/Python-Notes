file=open('file.txt','r')
text=open('text.txt','a+')

text.seek(0)
for data in text:
    print(data+'Before')

for data in file:
    text.write(data)

text.seek(0)
for data in text:
    print(data+" After")














