class A:

    def method_1(self):
        print("Class A : Method 1")
    def method_2(self):
        print("Class A : Method 2")

class B:

    def method_1(self):
        print("Class B : Method 1")

    def method_2(self):
        print("Class B : Method 2")

    def method_3(self):
        print("Class B : Method 3")

class C:

    def method_1(self):
        print("Class B : Method 1")

    def method_2(self):
        print("Class B : Method 2")

    def method_3(self):
        print("Class C : Method 3")
class D(A,B,C):   #MRO (method resolution order left to right dominance decreases )

    def method_1(self):
        print("Class C : Method 1")


d=D()
d.method_3()









