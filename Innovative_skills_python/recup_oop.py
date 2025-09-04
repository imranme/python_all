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

class Phone:
    manufactures = 'china'

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price
    
    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)

my_phone = Phone('khan', 'sumsung', 25999)
print(my_phone.owner, my_phone.brand, my_phone.price)


her_phone = Phone('she', 'iphpone', 32423493)
print(her_phone.owner)