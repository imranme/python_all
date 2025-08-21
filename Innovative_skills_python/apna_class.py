# # Class & Object in python

# # class is a blueprint for creating objects

# # creating class

# class Student:
#     name = "Tushar Khan"


# #creating object(instance)

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# #  creating car class 

# class car:
#     color = "blue"
#     brand = "mercedes"

#     # creating a car object
# car1 = car()
# print(car.color)
# print(car.brand)


# # creating class 

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# #  creating object

# s1 = Student("Tushar", 24)
# print(s1.name , s1.age)

# s2 = Student("Sabbir", 22)
# print(s2.age, s2.name)

    # class & instance Attributes 

# class Attributes
# instance Attribute

# class Student:
#     univercity_name = "Manarat International Univercity" # class Attributes eta memory te ak bar store hoy
#     # name = "anonymous" # class attr
#     def __init__(self, name, age):
#         self.name = name #(obj attr> class attr , same thakle obj age print hobe)# instance Attributes ektar jonno ek ek bar store hoy
#         self.age = age
#         print("affing new student in Database..")

# #  creating object

# s1 = Student("Tushar", 24)
# print(s1.name , s1.age)

# s2 = Student("Sabbir", 22)
# print(s2.age, s2.name)

# s3 = Student("Nasim", 21)
# print(s3.age, s3.name)

# print(s2.univercity_name)
# print(s1.univercity_name)
# print("Nasim Uni name",s3.univercity_name)

    # Methods

class Student:
    univercity_name = "Manarat International Univercity" 

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def welcome(self):
        print("welcome stident,",self.name)
    
    def get_age(self):
        return self.age  
      
s1 = Student("Tushar", 24)
s1.welcome()
print(s1.get_age())