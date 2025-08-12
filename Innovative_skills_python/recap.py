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

# Operators 
# . গাণিতিক অপারেটর (Arithmetic Operators): পাইথনে গাণিতিক কাজ করার জন্য বিভিন্ন অপারেটর রয়েছে।

# + : যোগ
# - : বিয়োগ
# * : গুণ
# / : ভাগ (ভাসা ভ্যালু রিটার্ন করে)
# // : ভাগফল (পূর্ণসংখ্যা রিটার্ন করে)
# % : ভাগশেষ (মডুলাস)
# ** : ঘাত (এক্সপোনেনশিয়াল)

x = 10
y = 3
print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.3333333333333335
print(x // y)  # 3
print(x % y)   # 1
print(x ** y)  # 1000


# ২. তুলনামূলক অপারেটর (Comparison Operators): তুলনামূলক অপারেটর ব্যবহার করে ভেরিয়েবল বা মানগুলোর মধ্যে তুলনা করা হয়, যা বুলিয়ান রেজাল্ট (True বা False) রিটার্ন করে।

# == : সমান কিনা যাচাই করে
# != : সমান নয় কিনা যাচাই করে
# < : ছোট কিনা
# > : বড় কিনা
# <= : ছোট বা সমান কিনা
# >= : বড় বা সমান কিনা
# উদাহরণ:

a = 5
b = 10
print(a == b)  # False
print(a != b)  # True
print(a < b)   # True
print(a > b)   # False
print(a <= b)  # True
print(a >= b)  # False

# ৩. লজিক্যাল অপারেটর (Logical Operators): লজিক্যাল অপারেটর ব্যবহার করে একাধিক শর্তের ভিত্তিতে একটি লজিক্যাল আউটপুট দেওয়া হয়।

# and : সব শর্ত True হলে True রিটার্ন করে
# or : যেকোনো একটি শর্ত True হলে True রিটার্ন করে
# not : শর্তের বিপরীত মান প্রদান করে

a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# এক্সপ্রেশন (Expressions):
# এক্সপ্রেশন হলো অপারেটর এবং অপারেন্ডের সংমিশ্রণ, যা একটি নির্দিষ্ট ফলাফল রিটার্ন করে। এক্সপ্রেশনগুলো পাইথনে অনেক ধরণের হতে পারে, যেমন গাণিতিক এক্সপ্রেশন, লজিক্যাল এক্সপ্রেশন ইত্যাদি।

# উদাহরণ:

# গাণিতিক এক্সপ্রেশন
x = 10
y = 5
result = x + y * 2  # এখানে x + (y * 2) হিসেবে এক্সপ্রেশনটি মূল্যায়ন করা হবে
print(result)       # 20

# লজিক্যাল এক্সপ্রেশন
a = True
b = False
logical_result = a or b and not a
print(logical_result)  # False

# সংক্ষেপে:
# অপারেটর হলো সেই চিহ্ন বা প্রতীক যা ভেরিয়েবল বা মানের মধ্যে বিভিন্ন ধরনের কাজ সম্পন্ন করে।
# এক্সপ্রেশন হলো অপারেটর ও অপারেন্ডের সমন্বয়ে গঠিত, যা একটি নির্দিষ্ট মান বা ফলাফল প্রদান করে।

a = 5  # 0101 in binary
b = 3  # 0011 in binary

# AND
print("AND:", a & b)    # Output: 1 (0001 in binary)

# OR
print("OR:", a | b)     # Output: 7 (0111 in binary)

# XOR
print("XOR:", a ^ b)    # Output: 6 (0110 in binary)

# NOT
print("NOT:", ~a)       # Output: -6 (in two's complement, 1010 in binary)

# Left Shift
print("Left Shift:", a << 1)  # Output: 10 (1010 in binary)

# Right Shift
print("Right Shift:", a >> 1) # Output: 2 (0010 in binary)


# সংক্ষেপে (Python Control Statements):

# Conditional Statements – শর্ত অনুযায়ী কোড চালানো

# if → শর্ত সত্য হলে কোড চালায়

# elif → আগের শর্ত মিথ্যা হলে নতুন শর্ত পরীক্ষা

# else → সব শর্ত মিথ্যা হলে চালায়

# Looping Statements – কোড বারবার চালানো

# for → নির্দিষ্ট সংখ্যা বা iterable এর উপাদান নিয়ে লুপ

# while → শর্ত সত্য থাকলে চলতে থাকে

# Jump Statements – লুপের প্রবাহ নিয়ন্ত্রণ

# break → লুপ সাথে সাথে বন্ধ

# continue → বর্তমান ইটারেশন বাদ দিয়ে পরেরটিতে যায়

# pass → কিছুই করে না, শুধু প্লেসহোল্ডার

# এগুলো প্রোগ্রামের প্রবাহ নিয়ন্ত্রণের মূল ভিত্তি।

# Conditional Statments 

# Conditional Statements
age = 17
if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You can vote in school elections.")
else:
    print("You are not eligible to vote.")

print("\n--- Looping and Jump Statements ---")

# Looping with for loop
for i in range(1, 6):
    if i == 3:
        continue  # ৩ স্কিপ করবে
    if i == 5:
        break     # ৫ এ থেমে যাবে
    print("Number:", i)

# While loop with pass
count = 0
while count < 5:
    if count == 2:
        pass  # কিছু করবে না, শুধু প্লেসহোল্ডার
    print("Count:", count)
    count += 1


while condition:

count  = 1
while count <= 5:
    print(count)
    count += 1

user_input = " "
while user_input != "stop"
    user_input = input("Enter sommething(type 'sotp' to exit): ")
    print("You entered:", user_input)


# # data structure 
# পাইথনে ডেটা স্ট্রাকচার হলো এমন কিছু উপাদান, যা ডেটা সংরক্ষণ এবং সংগঠিত করতে ব্যবহৃত হয়। এগুলো বিভিন্ন ধরনের ডেটাকে একটি নির্দিষ্ট কাঠামোর মধ্যে সাজিয়ে প্রোগ্রামিংকে সহজতর করে। পাইথনের প্রধান ডেটা স্ট্রাকচারগুলো হলো লিস্ট, টাপল, সেট, এবং ডিকশনারি।

# ১. লিস্ট (List)
# বর্ণনা: লিস্ট একটি পরিবর্তনযোগ্য (mutable) ডেটা স্ট্রাকচার, যেখানে এক বা একাধিক ডেটা আইটেম সংরক্ষণ করা যায়। লিস্টের মধ্যে যেকোনো ধরনের ডেটা রাখা যায় এবং এটি ইনডেক্সড হয়, অর্থাৎ প্রতিটি আইটেমের একটি নির্দিষ্ট অবস্থান থাকে।
# সিনট্যাক্স: [] বন্ধনীর মধ্যে ডেটা লিখে লিস্ট তৈরি করা হয়।
# উদাহরণ:

fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # আউটপুট: apple
fruits.append("orange")  # নতুন আইটেম যোগ করা
print(fruits)      # আউটপুট: ["apple", "banana", "cherry", "orange"]


# ২. টাপল (Tuple)
# বর্ণনা: টাপল একটি অপরিবর্তনযোগ্য (immutable) ডেটা স্ট্রাকচার, যেখানে একবার আইটেম সংরক্ষণ করলে তা পরিবর্তন করা যায় না। এটি লিস্টের মতই ইনডেক্সড এবং অর্ডার মেইন্টেইন করে, তবে টাপল পরিবর্তন করা যায় না।
# সিনট্যাক্স: () বন্ধনীর মধ্যে ডেটা লিখে টাপল তৈরি করা হয়।
# উদাহরণ:

coordinates = (10, 20)
print(coordinates[0])  # আউটপুট: 10
# টাপলে কোন আইটেম যোগ করা বা পরিবর্তন করা যায় না


# ৩. সেট (Set)
# বর্ণনা: সেট একটি অনন্য (unique) এবং অর্ডারলেস (unordered) সংগ্রহ, যেখানে প্রতিটি আইটেম একবারই থাকে। সেটে ডুপ্লিকেট আইটেম রাখা যায় না এবং ইনডেক্সিংও সম্ভব নয়।
# সিনট্যাক্স: {} বন্ধনীর মধ্যে ডেটা লিখে সেট তৈরি করা হয়।
# উদাহরণ:

unique_numbers = {1, 2, 3, 4, 4}
print(unique_numbers)   # আউটপুট: {1, 2, 3, 4}
unique_numbers.add(5)   # নতুন আইটেম যোগ করা
print(unique_numbers)   # আউটপুট: {1, 2, 3, 4, 5}


# ৪. ডিকশনারি (Dictionary)
# বর্ণনা: ডিকশনারি একটি কী-ভ্যালু (key-value) জোড়া ডেটা স্ট্রাকচার, যা মেমোরিতে ডেটা সংরক্ষণের জন্য ব্যবহার করা হয়। প্রতিটি আইটেমের একটি কী এবং তার মান থাকে। ডিকশনারির মাধ্যমে দ্রুত ডেটা খুঁজে পাওয়া যায়।
# সিনট্যাক্স: {} বন্ধনীর মধ্যে key: value জোড়া লিখে ডিকশনারি তৈরি করা হয়।
# উদাহরণ:

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(student["name"])   # আউটপুট: Alice
student["age"] = 21      # মান পরিবর্তন
print(student)           # আউটপুট: {'name': 'Alice', 'age': 21, 'grade': 'A'}

# ডেটা স্ট্রাকচারের তুলনা:
# ডেটা স্ট্রাকচার	ইনডেক্সিং	পরিবর্তনযোগ্যতা	ডুপ্লিকেট মান	সিনট্যাক্স
# লিস্ট	হ্যাঁ	পরিবর্তনযোগ্য	হ্যাঁ	[]
# টাপল	হ্যাঁ	অপরিবর্তনযোগ্য	হ্যাঁ	()
# সেট	না	পরিবর্তনযোগ্য	না	{}
# ডিকশনারি	কী দিয়ে	পরিবর্তনযোগ্য	কী অনন্য, মান হতে পারে	{key: value}
# সংক্ষেপে:
# লিস্ট: পরিবর্তনযোগ্য, ইনডেক্সড, এবং ডুপ্লিকেট মান গ্রহণযোগ্য।
# টাপল: অপরিবর্তনযোগ্য, ইনডেক্সড, এবং ডুপ্লিকেট মান গ্রহণযোগ্য।
# সেট: অনন্য মান সমর্থন করে এবং অর্ডারলেস।
# ডিকশনারি: কী-ভ্যালু জোড়া আকারে ডেটা সংরক্ষণ করে এবং দ্রুত অ্যাক্সেসের জন্য ব্যবহৃত হয়।
# এই ডেটা স্ট্রাকচারগুলো পাইথনে ডেটা সংরক্ষণ ও সংগঠিত করতে গুরুত্বপূর্ণ ভূমিকা পালন করে।

# list comprehenction 

# new_list = [expression for item in iterable if condition]

# normal list comprehencsion
numbers = [x for x in range(1, 11)]
print(numbers)