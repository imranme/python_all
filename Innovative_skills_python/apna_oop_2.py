#   del keyword 
class Student:
    def __init__(self, name):
        self.name= name

s1 = Student ("Tushar")
# print(s1.name)
# del s1.name
# print(s1.name)

# private att & method 
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("1234", "bdbank")
print(acc1.acc_no)
print(acc1.reset_pass)


class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")
    
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())