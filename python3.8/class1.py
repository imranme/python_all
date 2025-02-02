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
marks = int(input("what is your marks i programming: "))

def show_grade(grade):
    print(f"You got: {grade}")

if marks >= 80:
    show_grade("A+")
elif marks < 80 and marks >= 70:
    show_grade("A")
elif marks < 70 and marks >= 60:
    show_grade("A-")
elif marks > 33:
    show_grade("C")
else:
    show_grade("F")

print("end")









