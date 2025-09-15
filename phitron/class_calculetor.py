class Calculator:
    # ক্লাস অ্যাট্রিবিউট
    brand = "Casio MS900"

    # যোগফল
    def add(self, num1, num2):
        return num1 + num2

    # বিয়োগফল
    def deduct(self, num1, num2):
        return num1 - num2

    # গুণফল
    def multiply(self, num1, num2):
        return num1 * num2

    # ভাগফল
    def divide(self, num1, num2):
        if num2 == 0:     # ভাগ শূন্য হলে Error এড়াতে
            return "Cannot divide by zero"
        return num1 / num2


# অবজেক্ট তৈরি
calc = Calculator()

print("Brand:", calc.brand)
print("Add:", calc.add(10, 5))
print("Deduct:", calc.deduct(10, 5))
print("Multiply:", calc.multiply(10, 5))
print("Divide:", calc.divide(10, 5))
