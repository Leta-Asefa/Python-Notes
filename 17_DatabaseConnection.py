import mysql.connector
host='localhost'
user='root'
password=''
database='student'

connection=mysql.connector.connect(host='localhost',user='root',password='',database='student',port='3300')
cursor=connection.cursor()

if connection.is_connected():
    print('Connected to MySQL')
    query = 'insert into student value(54,"Teka","Mechanical")'
    cursor.execute(query)
    query='select * from student'
    cursor.execute(query)
    result=cursor.fetchall()
    for data in result:
        print(data)

else:
    print('Failed')











