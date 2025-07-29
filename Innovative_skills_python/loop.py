# Example 1: Print the first 10 natural numbers using for loop.
n = 12
for i in range(0, n):
    print(i)

# Example 2: Python program to print all the even numbers within the given range.

given_range = 10
for i in range(given_range):
    if i%2 == 0:
        print(i)

# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.

given_number = 10

sum = 0

for i in range(1,given_number+1):
    sum+=i
print(sum)

# Example 4: Python program to calculate the sum of all the odd numbers within the given range.
given_range = 10
sum = 0

for i in range(given_range):
    if i%2!=0:
        sum += i
    
print(sum)

# Example 5: Python program to print a multiplication table of a given number 

given_number = 5

for i in range(11):
    # print(given_number,"x",i,"=",5*i)
    result = given_number * i
    print(f"{given_number} x {i} = {result}")

# Example 6: Python program to display numbers from a list using a for loop. 

list=[1,2,3,4,66,787]
for i in list:
    print(i)

# Example 7: Python program to count the total number of digits in a number.

given_number = 12343254

given_number = str(given_number)

count = 0

for i in given_number:
    count += 1

print(count)

# Example 8: Python program to check if the given string is a palindrome.

given_string = "madam"
 

reverse_string = ""
 

for i in given_string:
    reverse_string = i + reverse_string  
 
if(given_string == reverse_string):
   print("The string", given_string,"is a Palindrome.")
 
else:
   print("The string",given_string,"is NOT a Palindrome.")

# Example 9: Python program that accepts a word from the user and reverses it.

given_string = input()

reverse_string = ""

for i in given_string:
    reverse_string = i + reverse_string

print(reverse_string)

# Example 10: Python program to check if a given number is an Armstrong number 

# the given number
given_number = 153
 
# convert given number to string
# so that we can iterate through it
given_number = str(given_number)
 
# store the lenght of the string for future use
string_length = len(given_number)
 
# initialize a sum variable with
# 0 value to store the sum of the product of
# each digit
sum = 0
 
# iterate through the given string
for i in given_number:
    sum += int(i)**string_length
 
# if the sum matches the given string
# its an amstrong number
if sum == int(given_number):
    print("The given number",given_number,"is an Amstrong number.")
 
# if the sum do not match with the given string
# its an amstrong number
else:
    print("The given number",given_number,"is Not an Amstrong number.")

sum_odd = 0
sum_even  = 0

for i in range(1, 11):
    if(i%2 == 1):
        sum_odd = sum_odd +i
    else:
        sum_even = sum_even +i

print("the sum of all odd numbers: ", sum_odd)
print('the sum od all even number: ', sum_even)
