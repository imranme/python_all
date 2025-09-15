class Dog:
    def __init__(self, _name, _age, _color):
        self.name = _name
        self.age = _age
        self.color = _color
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    def get_color(self):
        return self.color
    def bark(self):
        print('Huff')

mydog = Dog('Bagha', 2, 'brown')
mydog.bark()

print(mydog.get_age())

class Person:
    # """
    # একটি Person অবজেক্টের মধ্যে থাকবে:
    #   - first_name
    #   - last_name
    #   - gender
    #   - address
    # এবং describe_user() মেথড সেই ব্যক্তির নাম ও ঠিকানা দেখাবে।

    # কনস্ট্রাক্টর: অবজেক্ট তৈরি হলে এট্রিবিউট সেট করবে
    def __init__(self, first_name, last_name, gender, address):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.address = address

    # ব্যবহারকারীর তথ্য প্রিন্ট করবে
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} lives in {self.address}")


# অবজেক্ট তৈরি
person1 = Person("Alamgir", "Hossain", "male", "Ramna Thana")

# মেথড কল
person1.describe_user()

person2 = Person('khan', 'imran', 'male', 'mirpur')
person2.describe_user()

if person1 == person2:
    print("They are the same person")
else:
    print("They are different peesone")
