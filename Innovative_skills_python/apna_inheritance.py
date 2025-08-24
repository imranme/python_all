# Inheritance Types: 1: Single Inheritance
#                    2:Multi-level Inheritance
#                    3:Multiple inheritanec



    # Single Inheritance work flow : bass (Base)=> derivel(child)
class Car:
    # color = "black"
    @staticmethod
    def strat():
        print("car strated..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.color)

class Fortuner(ToyotaCar): #Multi-level inheritance
    def __init__(self, type):   
        self.type = type
    
car1 = Fortuner("diesel")
car1.strat()

# Multiple inheritanec

class A:
    varA = "Welcome class A"

class B:
    varB = "Welcome class B"

class C(A, B):
    varC = "Welcome class C"

c1= C()

print( c1.varC,'\n',c1.varB,'\n',c1.varA)