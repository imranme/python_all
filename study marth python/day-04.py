# >>> "We love python!"
# 'We love python!'
# >>> 'The most popular general purpose programming language'
# 'The most popular general purpose programming language'


# >>> input("Give me your country name: ")
# Give me your country name: Bangladesh
# 'Bangladesh'



# All About Data Types in Python 

# Numeric Data 
# Boolean Data
# Sequece Data 
# Set Data 
# Mapping Data 
# Data Frame 


# all about data types in python
    # Numeric Data --> 1. int, 2.float, 3.complex


x  = 10  # int
y  =  20.4 # float
z  =   10+6j # 1o is real number and 6j is integer

print(type(x))
print(type(y))
print(type(z))

print(isinstance(z,complex)) 
print(isinstance(11,complex)) 

n = complex(input('Enter your complex number:- '))
print(n)

        # Boll 

x = True
y = False

print(x)
