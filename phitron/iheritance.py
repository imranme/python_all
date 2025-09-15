    #  inheritance 

class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def attack(self):
        print('I am attacking...')


class Fogthing(Monster):
    def make_sound(self):
        print('Grrrrrrrrrr\n')


class Mournsnake(Monster):
    def make_sound(self):
        print('Hiiissssshhhh\n')


fogthing = Fogthing("Fogthing", "Yellow")
fogthing.attack()
fogthing.make_sound()

mournsnake = Mournsnake("Mournsnake", "Red")
mournsnake.attack()
mournsnake.make_sound()

    # অভাররাইড

class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def attack(self):
        print('I am attacking...')


class Fogthing(Monster):
    def attack(self):
        print('I am killing...')

    def make_sound(self):
        print('Grrrrrrrrrr\n')


fogthing = Fogthing("Fogthing", "Yellow")
fogthing.attack()
fogthing.make_sound()

#    মাল্টিপল ইনহেরিট্যান্স

class A:
    def where(self):
        print("I am from class A")


class B:
    def where(self):
        print("I am from class B")


class C(A, B):
    pass

an_instance_of_c = C()
an_instance_of_c.where()

#    super মেথড

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()