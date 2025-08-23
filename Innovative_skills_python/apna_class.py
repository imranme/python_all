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

class Student:
    univercity_name = "Manarat International Univercity" 

    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    # class student:
    #     @staticmethod
    #     def college():
    #         print("Hello Tushar")

    def welcome(self):
        print("welcome stident,",self.name)
    
    def get_age(self):
        return self.age  
      
s1 = Student("Tushar", 24)
print(s1.get_age())

s1.name = "imran"
s1.welcome()



# s2 = Student("Tushar imran", 24)
# s2.welcome()
# print(s2.get_age())  

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @staticmethod #decorator
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)
s1 = Student("tony strk", [99, 98, 97])
s1.get_avg()
s1.hello()

s1.name = "khan"
s1.get_avg()

# let's practice 

# create Account class with 2 attributes - balance & account no.
# create method for debit , credit & printing the balance.

class Account:
    def __init__(self, blance, account):
        self.blance = blance
        self.account = account
    #debit method
    def debit(self, amount):
        self.blance -= amount
        print("TK.", amount, "was debited")
        print("total balance = ", self.get_balance())
    
    def credit(self, amount):
        self.blance += amount
        print("TK.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.blance
    

acc1 = Account(100000, 1234)
acc1.debit(2000)
acc1.credit(1000)
acc1.credit(200003)
acc1.debit(1999)