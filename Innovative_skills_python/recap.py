# variable 
# ভেরিয়েবল হলো ডেটা সংরক্ষণের জন্য নামকরণ করা স্থান। পাইথনে ভেরিয়েবল ডিক্লেয়ার করার জন্য কোনো বিশেষ কিওয়ার্ডের প্রয়োজন নেই; সরাসরি ভেরিয়েবলে মান অ্যাসাইন করলেই এটি তৈরি হয়।

name = "Aline"
age = 25
temperature= 40.9


# এই উদাহরণে, name, age, এবং temperature হলো ভেরিয়েবল, যা বিভিন্ন ডেটা সংরক্ষণ করছে।

# Data Types 
# int age= 25
# folat 90.9
#string = "tuhsar"
#bool = true or false
#list=[1,2,3,4,5]
# tuple (20.0,.20.0)
#dict = {"name": "imran", "age": 24}
# type() chek


# input 
# ইউজারের কাছ থেকে ডেটা সংগ্রহ করার জন্য পাইথনে input() ফাংশন ব্যবহার করা হয়। এটি সাধারণত টেক্সট আকারে ইনপুট নেয় এবং ডেটা টাইপ হিসেবে string রিটার্ন করে। প্রয়োজনে এই ইনপুটকে int, float ইত্যাদি টাইপে কনভার্ট করা যায়।

name = input("Enter yoor name: ")
print("hello, " + name)

age = int(input("Enter your age: "))
print('Your age is', age)

# output: পাইথনে আউটপুট প্রদর্শন করতে print() ফাংশন ব্যবহার করা হয়। এটি বিভিন্ন ধরনের ডেটা আউটপুটে প্রদর্শন করতে পারে।

name = "Alice"
age = 25
print("Name:", name)
print("Age:", age)

# ফরম্যাটিং সহ আউটপুট: পাইথনে আউটপুটকে আরো সুন্দরভাবে প্রদর্শনের জন্য f-string বা format() মেথড ব্যবহার করা যায়।

# f-string 
name = "Tushar"
age = 24
print(f"Hello, {name}. You are {age} years old.")
# format() method 
print("Hello, {}. You are  {} years old.".format(name, age))

# সংক্ষেপে:
# ইনপুট নেওয়ার জন্য: input() ফাংশন ব্যবহার করা হয়।
# আউটপুট প্রদর্শনের জন্য: print() ফাংশন ব্যবহার করা হয়।

