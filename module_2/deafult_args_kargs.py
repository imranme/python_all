#args
def all_sum(*numbers):
    print(numbers)

total = all_sum(43, 44, 66, 12)
print('all sum: ', total)

def sum(num1, num2, num3=0, num4=0, num5=0):
    result = num1 + num2 + num3 + num4 + num5
    return result

total = sum(99, 11, 5)

# def function_name (num1, num2, *args, **kargs):

# return multiple things from an array

def a_lot(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    return sum, mult, remain