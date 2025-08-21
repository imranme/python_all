# Class & Object in python

# class is a blueprint for creating objects

# creating class

class Student:
    name = "Tushar Khan"


#creating object(instance)

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

#  creating car class 

class car:
    color = "blue"
    brand = "mercedes"

    # creating a car object
car1 = car()
print(car.color)
print(car.brand)


# creating class 

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


#  creating object

s1 = Student("Tushar", 24)
print(s1.name , s1.age)

s2 = Student("Sabbir", 22)
print(s2.age, s2.name)