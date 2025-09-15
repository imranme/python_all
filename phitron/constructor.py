class Phone:
    menufactured = 'banglades'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.pirce = price
    
    def send_sms(self, phone, sms):
        text = f'sending to:{phone}{sms}'
        print((text))

my_phone = Phone('Tushar imran', 'OOP', 23424)
print(my_phone.owner, my_phone.brand, my_phone.pirce)

my_phone2= Phone('Tushar imran khan', 'Iphone', 20000000)   
print(my_phone2.owner, my_phone2.brand, my_phone2.pirce)

my_phone.send_sms("435843535755", "hello kmn aso?")


