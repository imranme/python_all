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