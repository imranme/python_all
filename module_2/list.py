# index = 0 1 2 3 4 5 
numbers =[ 12 , 34, 45, 54, 65]

# index = -5, -4, -3, -2, -1 

print (numbers[3], numbers[-3])

# list (strat : end) # strat from the strat index and stops befor the end index

print(numbers[2:6])


# list(strat : end : step)
print(numbers[1:7:1])
print(numbers[:]) # shortcut to copy a list
print(numbers[::-1]) # shortcut to reverse a list