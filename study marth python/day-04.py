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


# x  = 10  # int
# y  =  20.4 # float
# z  =   10+6j # 1o is real number and 6j is integer

# # print(type(x))
# # print(type(y))
# # print(type(z))

# print(isinstance(z,complex))/
# # print(isinstance(11,complex))

# n = complex(input('Enter your complex number:- '))
# print(n)/

#         # Boll 

# x = True
# y = False

# print(x)


    # Sequence Data 

        #  List 

# l =[1,2,3,4,True,[1,2],'data',(1,2,3,8)]
# print(l[2])
# print(l[-1])
# print(l[-1][-1])
# print(type(l))
# print(isinstance(l,list))

    #Tuple
t = (1,5,8,9,'ai')
print(t)
print(type(t))
print(t[0])
print(t[0:4]) #colon means to; 0 to 4-1

 #Range()

x = range(10) #1st case
print(x)
for i in x:
    print(i)


    

x = range(5, 20, 3)
for i in x:
    print(i)


x = range(20,5,-3) #4th case
for i in x:
    print(i)


#array
import array as ar



a = ar.array('i',[1,2,3,4])
print(a)
print(type(a))

a = ar.array('f',[1.5,2,3,4])
print(a)


#string
x = 'data'
print(type(x))

x = '''
I love
Data Science
'''
print(x)
print(type(x))

#Set

s = {1,2,3,5}
print(s)
print(type(s))

# sequence Data 

# list 
l = 