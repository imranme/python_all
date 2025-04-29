print('hello world', 'welcome to 60 days of python', sep='&', end='|')

var = "hello world"
print(var)
print('My Sentence is ' +var)

name = 'Tushar'
print(name)


#  locals vs global variable

x = 2000 #global

def func1():
    x = 500 #local
    print('My num is: ', x)
func1()
print('My num is: ',x)


def func1():
    global x
    x = 500 #local
    print('My num is: ', x)
func1()
print('My num is: ',x)

y = 1000
def func2():
    t=100
    print('My Num is: ', y)
func2()
print('My num is:', y)