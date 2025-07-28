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