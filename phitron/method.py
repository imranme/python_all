def call():
    print('calling someone i dont know')
    return 'call done'

class phone:
    price = 2000
    color = 'blue'
    brand = 'sumsunge'

    def call(self):
        print("calling one persone")
    
    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text
    
my_phone = phone()
print(my_phone.brand)
my_phone.call()
result = my_phone.send_sms(32434, 'hello its my phone')
print(result)