def show_double(x):
    print(x*2)

show_double(2)
show_double(100)


# পাইথনে * এর অর্থ
# * এর আর্গুমেন্টে ভ্যালু Tuple হিসেবে প্যাকড থাকে। এর মানে * দিয়ে প্যারামিটার ডিক্লেয়ার করলে আমরা যেকোন সংখ্যক পজিশনাল আর্গুমেন্ট পাস করতে পারি। যেমন করলাম make_sum এর ক্ষেত্রে। শুরুতে make_sum মাত্র দুইটা আর্গুমেন্ট নিলেও পরবর্তীতে আমরা প্যারামিটারে * বসিয়ে দিলাম তখন সে অনেকগুলো আর্গুমেন্ট পাস করতে পারছে।

def make_sum(*args):
    sum = 0
    for num in args: # Here, args is like a Tuple which is (10, 20, 30, 40)
        sum += num
    return sum

print(make_sum(10, 20, 30, 40))

def add_numbers(x, y):
    total = x + y
    return total
       

print(add_numbers(4, 5))


# এক্সেপশন 

a = 2500
b = 0

print(a/b)
print("I did it")



try:
    a = 1000
    b = int(input("Enter a divisor to divide 1000: "))
    print(a/b)
except ZeroDivisionError:
    print("You entered 0 which is not permitted!")


try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Type or value error occurred")


try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")

try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")


 print("Hello")
raise NameError('HiThere')


print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)


def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))

file_to_work = open("filename.txt", "w")
# do HERE whatever you like, with the file
# such as write new lines in it

# then close it
file_to_work.close()