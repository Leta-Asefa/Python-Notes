class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayInfo(self):
        print('Name = ', self.name)
        print('Age = ', self.age)


class Student(Person):
    def __init__(self, name, age, department, year):
        self.department = department
        self.year = year
        Person.__init__(self, name, age)


Abebe = Student('Abebe', 23, 'IT', '3rd')
Abebe.displayInfo()

Kebede = Student('Kebede', 22, 'CS', '2rd')
Kebede.displayInfo()