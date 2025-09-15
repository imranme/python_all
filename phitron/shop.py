class Shop:
    shopping_mall = 'Jamuna'
    # cart = [] # is a class attribute
    def __init__(self, buyer): 
        self.buyer = buyer
        self.cart = []   # cart is an instance attribute
    def add_to_cart(self, item): #method
        self.cart.append(item)

noman = Shop('noman khan')
noman.add_to_cart('shoes')
noman.add_to_cart('phone')
print(noman.cart)


chatrolig = Shop('helmate')
chatrolig.add_to_cart('bass')
chatrolig.add_to_cart('hatur')
print(chatrolig.cart)


