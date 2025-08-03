def hello_fun():
    print("hello, first fun")

hello_fun()

# প্যারামিটার সহ ফাংশন

def greet(name):
    print("Hello, " + name + "!")
greet("Alice")

# return function 

def add(a, b):
    return a + b
result = add(5, 3)
print("Result: ", result)

# parameter function 
def greet(name="Gust"):
    print("Hello, " + name + "!")
greet()
greet("Bob!")


# lambda function seentax: lambda arguments: expressoim

add = lambda x, y: x + y
print(add(5 , 3))

# defult parameter function 

def greet(name = " Gust"):
    print("Hello, " + name + "!")
greet()
greet("Bob!")

# Positional Arguments 
def add(a, b):
    return a + b
print(add(5, 3))

# keword arguments

def introduce(name, age):
    return f"My name is {name} and I an {age} year's old."
print(introduce(age=25, name="Rokibul"))

# Default Parameter 
def greet(name="Guest"):
    return "Hello, " + name
print(greet())
print(greet("Rokibul kaka"))

# variable-length arguments
def add(*numbers):
    return sum(numbers)
print(add(1, 2, 3, 4, 5))

# return value 
def function_name(parametars):
    #code area
    return result

# within return value 

def add(i, j):
    result = i + j
    return result
sum_value = add(5, 6)
print("Sum: ", sum_value)

# without return Value
def greet(name):
    print("Hello, " + name + "!")

result = greet("Alice")
print(result) 

# multipul return value 
def calculate(a, b):
    sum_value = a + b
    diff_value = a - b
    return sum_value, diff_value
result_sum, result_diff = calculate(10, 5)
print("Sum: ", result_sum)
print("Difference: ", result_diff)


# decorator and genarator 
def decorator_function(orginal_function):
    def wrapper_fuction():
        orginal_function()
    return wrapper_fuction


def my_decprator(func):
    def wrapper():
        print("Function is about to execut.")
        func()
        print("Function has executed.")
    return wrapper
@my_decprator
def say_hello():
    print("hello World!")
say_hello()


# genaretor

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # আউটপুট: 1
print(next(gen))  # আউটপুট: 2
print(next(gen))  

def count_down(n):
    while n > 0:
        yield n
        n -= 1

for number in count_down(5):
    print(number)



# lambda arguments : expression

add = lambda a, b: a + b
print(add(5, 3))   # Output: 8


square = lambda x: x * x
print(square(4))   # Output: 16



points = [(1, 2), (4, 1), (3, 5), (2, 0)]
points_sorted = sorted(points, key=lambda x: x[1])
print(points_sorted)


nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # Output: [2, 4, 6]







































        





























































































































































































































































































































































































































