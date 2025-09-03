class Bangladesh:
    batt = "Litton"
    run = 52
    opponet = "Netherland"

my_teame = Bangladesh()

print(my_teame)
print(my_teame.opponet)

class Calculator:
    # class attribute
    brand = "Casio MS990"
    
    # instance method
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
calc = Calculator()

print("Brand: ", calc.brand)
