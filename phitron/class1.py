# username = input("Your name: ")

# print(f"hello {username}!")

# print("hello world") #first code python 3.8

        #Function/

# print("1")

# def complicated_logic(first, second):
#     print(f"You passed: {first}, {second}")

# number_1 = 10
# number_2 = 3

# print("2")
# complicated_logic(number_1, number_2)
# complicated_logic(5, 4)
# print("3")

    # Data type 

# number_value = 32
# second_value = 4

# addition = number_value + second_value
# subtraction = number_value - second_value
# mul = number_value* 2
# div = number_value / 5
# div_int = number_value // 2
# remainder = number_value % 5

# print(f"div: {div_int}")
# print(f"rem: {remainder}")

# print(f"Addtion: {addition}")
# print(f"Sub: {subtraction}")

# person_name = "Zulkarnine Mahmud"
# food = "burger"
# value2 = 99

# name_value = person_name + " " + str(value2)
# concatenated_strig = person_name + food
# print(concatenated_strig)
# print(name_value)
# print(f"Legth of name: {len(name_value)}")


        # list 

# grocery_list = ["rice", "potato", "tomato"]
# l2 = list()
# secod_item = grocery_list[1]
# print(grocery_list)
# print(secod_item)
# grocery_list.append("water")

# print(grocery_list)
# print(l2)
# l2.append(3)
# print(l2)
# l2.append("computer")
# print(l2)
# print(grocery_list[-1]) # it's a chek last umber of list python, (-1 = 3) is a same index number


# number_list = [1,90,34,23,77,21,12,67,89,44,50] 
# number_list.sort() # sort the list
# print(number_list)

    # input / Output python 
# name_country = input("Give me your country name: ")
# print("may country name:",name_country)

    # conditions 
# marks = int(input("what is your marks i programming: "))

# def show_grade(grade):
#     print(f"You got: {grade}")

# if marks >= 80:
#     show_grade("A+")
# elif marks < 80 and marks >= 70:
#     show_grade("A")
# elif marks < 70 and marks >= 60:
#     show_grade("A-")
# elif marks > 33:
#     show_grade("C")
# else:
#     show_grade("F")

# number = int(input("Give a number: "))
# the_user_is_good = number >= 80
# message = "The number is greater than or equals 80; " +str(the_user_is_good)
# print(message)

# a = 330
# b = 330

# print("A") if a > b else print("=") if a == b else print("B")


    #  Eeven or odd 
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
# even_number = []
# starting = 0
# user_input = int(input("Limit: "))
# # while starting < user_input:
# #     if is_even(starting):
# #         even_number.append(starting)
# #     #     print(f"{starting} is Even")
# #     # # else:
# #     #     print(f"{starting} is Odd")
# #     starting = starting + 1

# for num in range(0, user_input):
#     if is_even(num):
#         even_number.append(num)

# print(f"Even umber: {even_number}")
# print("End")
    
# grocery_list = ["rice", "potato", "tomato"]

# for item in grocery_list:
#     if item == "potato":
#         break
#     print(item)

    # File Io 

# with open("/home/tushar/python_all/python3.8/python.txt", mode="r") as s_file:
#     words_all = []
#     for line in s_file.readlines():
#         words = line.strip(" ")
#         words_all += words
#     unique_words = set(words_all)
#     print(len(words_all))
#     print(len(unique_words))

#     with open("unique_words.text", mode="w") as write_file:
#         for item in sorted(unique_words):
#             write_file.write(item)
#             write_file.write("\n")

# print("End program")


        # debugging 

# '{2}, {1}, {0}'.format('a', 'b', 'c')
# 'c, b, a'
# '{0}{1}{0}'.format('abra', 'cad')
# 'abracadabra'

# message = "If x = {x} and y = {y}, then x+y = {z}".format(x = 20, y = 300, z = 20+300)

# print(message)


# if 10 > 5:
#     print("10 greater than 5") # এই স্টেটমেন্টটি if কন্ডিশনের এর আওতাভুক্ত
#     print("IF scope finished")    # এই স্টেটমেন্টটিও if কন্ডিশনের এর আওতাভুক্ত

# print("Program ended") # এই স্টেটমেন্টটি if কন্ডিশনের এর আওতাভুক্ত নয়


    # নেস্টেড if 

# num = 12
# if num > 5:
#     print("Bigger than 5")
#     if num <= 47:
#         print("Between 6 and 47")


# words = ["Hello", "world", "!"]
# print(words[0])
# print(words[1])
# print(words[2])

# number = 1
# my_numbers = [number, 2, 3]

# things = ["Numbers", 0, my_numbers, 4.56]

# print(things[0])
# print(things[1])
# print(things[2])
# print(things[2][2])

# def my_func(x = None):
#     if x:
#         return x * x
#     else:
#         return 0

# print(my_func())
# print(my_func(5))

# permissions = (("Admin", "Operator", "Customer"), ("Developer", "Tester"), [1, 2, 3], {"Stage": "Development"})

# print(permissions[3]["Stage"])

#     # tapoll unpacking

# numbers = (1, 2, 3)
# a, b, c = numbers
# print(a)
# print(b)
# print(c)


# a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# print(b)
# print(c)
# print(d)


# squares = [1, 2, 5, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 4, 6, 7, 8]
# print(squares[3:-4])


def make_sum(*args):
    sum = 0
    for num in args: # Here, args is like a Tuple which is (10, 20, 30, 40)
        sum += num
    return sum

print(make_sum(10, 20, 30, 40))
