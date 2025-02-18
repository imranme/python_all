a = b + c  #normal oparations

a = b.__add__(c) # oparator overloding

class MyNum():
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return (self.value * 2) + (other.value * 2)


a = MyNum(2)
b = MyNum(3)

c = a + b

print(c)


class MyInt():
    def __init__(self, value):
        self.__value = value

    def __int__(self):
        return self.__value

    def __add__(self, other):
        return self.__value + int(other) * int(other)


a = MyInt(2)
b = MyInt(3)

c = a + b

print(c)


class MyInt():
    def __init__(self, value):
        self.__value = value

    def __int__(self):
        return self.__value


    def __iadd__(self, other):
        return self.__value + int(other) * int(other)


a = MyInt(2)

a += MyInt(3)

print(a)


## Definition
class Add:
## Initialization
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
obj = Add(3,4)
## Access
print obj.add()
## Garbage collection

def add_explanation(line):
    return line + '!'

update_line = add_explanation

print(update_line("Hello World"))

def beautify(text):
    return text + '!!!'


def make_line(func, words):
    return "Hello " + func(words)


print(make_line(beautify, "world"))

