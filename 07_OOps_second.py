class Computer:
    brand="HP"
    def __init__(self,core,ram):
        self.core=core
        self.ram=ram
    @classmethod
    def getBrand(cls):
        return cls.brand

    @staticmethod
    def getInfo():
        print('do stm that is not related with either the object or the class')


c1=Computer('i3','8GB')

print(c1.getBrand())
Computer.getInfo()

