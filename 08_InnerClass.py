#e.g students have laptops : use inner class only if laptops will be used with students not with other classes
class Student:
    def __init__(self,name ,age,brand,ram):
        self.name=name
        self.age=age
        self.laptop=self.Laptop(brand,ram)

    def getInfo(self):
        print(self.name,self.age,self.laptop.brand,self.laptop.ram)
    class Laptop:
        def __init__(self,brand,ram):
            self.brand=brand
            self.ram=ram




s=Student('abebe',44,"HP","8GB")
s.getInfo()