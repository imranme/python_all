১. Conditions (শর্ত)

🔹 Q: if আর elif এর মধ্যে পার্থক্য কী? (Difference between if and elif?)

বাংলা উত্তর: if প্রথম শর্ত চেক করে, আর elif তখন চেক করে যখন আগের if বা elif False হয়।

English: if checks the first condition, and elif (else if) checks only if the previous ones are False.

x = 10
if x > 15:
    print("Greater than 15")
elif x > 5:
    print("Greater than 5")  # ✅ Runs


🔹 Q: if কি else ছাড়া ব্যবহার করা যায়? (Can if be used without else?)

বাংলা উত্তর: হ্যাঁ, if একা ব্যবহার করা যায়, else বাধ্যতামূলক না।

English: Yes, if can be used without else.

if x > 0:
    print("Positive number")


🔹 Q: পাইথনে এক লাইনে if-else কিভাবে লেখা যায়? (One-liner if-else?)

বাংলা উত্তর: এক লাইনে লিখতে হলে conditional expression ব্যবহার করতে হয়।

English: Use conditional expressions (ternary operator).

result = "Even" if x % 2 == 0 else "Odd"


🔹 Q: if condition-এ non-boolean value দিলে কী হয়? (Non-boolean in if condition?)

বাংলা উত্তর: Python truthy/falsey ধরে নেয়। যেমন 0, "", [], None → False।

English: Python treats values as truthy or falsy.

if []:
    print("True")
else:
    print("False")  # ✅


🔹 Q: একাধিক শর্ত কিভাবে চেক করা যায়? (Multiple conditions?)

বাংলা উত্তর: and, or, not ব্যবহার করে।

English: Use and, or, and not.

if x > 5 and x < 20:
    print("Between 5 and 20")

২. Lists (লিস্ট)

🔹 Q: লিস্ট কিভাবে তৈরি করা হয়? (How do you create a list?)

বাংলা উত্তর: [] ব্যবহার করা হয়।

English: Use square brackets [].

my_list = [1, 2, 3]


🔹 Q: লিস্ট আর টাপলের মধ্যে পার্থক্য কী? (List vs Tuple?)

বাংলা উত্তর: লিস্ট mutable (পরিবর্তনযোগ্য), টাপল immutable (পরিবর্তনযোগ্য নয়)।

English: List is mutable, Tuple is immutable.

my_list = [1,2,3]
my_tuple = (1,2,3)


🔹 Q: লিস্টে কিভাবে নতুন উপাদান যোগ করা হয়? (Append element?)

my_list.append(5)


🔹 Q: append() আর extend()-এর মধ্যে পার্থক্য কী?

বাংলা উত্তর: append() → একটাই উপাদান যোগ করে। extend() → সব উপাদান যোগ করে।

English: append() adds a single element, extend() adds multiple elements.

a = [1,2]
a.append([3,4])   # [1,2,[3,4]]
a.extend([3,4])   # [1,2,3,4]


🔹 Q: লিস্ট থেকে ডুপ্লিকেট কীভাবে সরানো যায়? (Remove duplicates?)

unique = list(set([1,2,2,3,4,4]))


🔹 Q: reverse() ছাড়া লিস্ট উল্টানো যায় কিভাবে? (Reverse without reverse?)

print(my_list[::-1])


🔹 Q: লিস্ট কম্প্রিহেনশন কী? (List comprehension?)

বাংলা উত্তর: এক লাইনে নতুন লিস্ট বানানোর শর্টকাট।

English: A concise way to create lists.

squares = [x*x for x in range(5)]


🔹 *Q: লিস্টকে 3 করলে কী হয়? (Multiply list by 3?)

বাংলা উত্তর: লিস্ট রিপিট হবে।

English: The list repeats.

print([1,2]*3)  # [1,2,1,2,1,2]

৩. For Loop (লুপ)

🔹 Q: লিস্টের index আর value একসাথে কিভাবে পাওয়া যায়? (Index + value iteration?)

for i,v in enumerate(["a","b","c"]):
    print(i,v)


🔹 Q: for loop এর সাথে else ব্যবহার করা যায় কি? (For with else?)

বাংলা উত্তর: হ্যাঁ, লুপ শেষ হলে else চালু হয় যদি break না হয়।

English: Yes, else runs if the loop finishes without a break.

for i in range(3):
    print(i)
else:
    print("Loop finished")


🔹 Q: লুপ থেকে আগেই বের হতে চাইলে কী করব? (Break loop?)

for i in range(5):
    if i==3: break


🔹 Q: break, continue, pass এর মধ্যে পার্থক্য কী?

বাংলা উত্তর:

break → লুপ থামায়

continue → বর্তমান iteration স্কিপ করে

pass → কিছুই করে না

English:

break stops loop

continue skips iteration

pass does nothing

🔹 Q: range(5) কিভাবে কাজ করে?

বাংলা উত্তর: ০ থেকে ৪ পর্যন্ত সংখ্যা তৈরি করে, lazy sequence।

English: Creates numbers 0 to 4 as a lazy sequence.

🔹 Q: dictionary-এর key আর value কিভাবে লুপ করা যায়?

for k,v in {"a":1,"b":2}.items():
    print(k,v)

৪. Functions (ফাংশন)

🔹 Q: ফাংশন কিভাবে ডিফাইন করা হয়? (Define function?)

def greet(name):
    return "Hello " + name


🔹 Q: return আর print()-এর মধ্যে পার্থক্য কী?

বাংলা উত্তর: return ভ্যালু ফেরত দেয়, print() শুধু দেখায়।

English: return returns value, print() displays it.

🔹 Q: ডিফল্ট আর্গুমেন্ট কী? (Default argument?)

def greet(name="Guest"):
    print("Hello", name)


🔹 Q: Mutable default argument-এর সমস্যা কী?

বাংলা উত্তর: লিস্ট/ডিকশনারি দিলে সেটা শেয়ার হয়ে যায়।

English: Mutable defaults are shared across calls.

🔹 **Q: *args আর kwargs-এর মধ্যে পার্থক্য কী?

বাংলা উত্তর: *args → positional arguments, **kwargs → keyword arguments নেয়।

English: *args collects positional, **kwargs collects keyword arguments.

🔹 Q: ফাংশন কি একাধিক ভ্যালু রিটার্ন করতে পারে? (Multiple return?)
👉 হ্যাঁ।

def calc(x,y):
    return x+y, x-y

৫. Dictionaries (ডিকশনারি)

🔹 Q: ডিকশনারি কিভাবে তৈরি করা হয়? (Create dictionary?)

my_dict = {"name":"Tushar","age":22}


🔹 Q: KeyError ছাড়াই ভ্যালু কিভাবে অ্যাক্সেস করব? (Safe access?)

print(my_dict.get("age","Not Found"))


🔹 Q: dict.get() আর normal access এর মধ্যে পার্থক্য কী?

বাংলা উত্তর: dict["key"] KeyError দেয়, get() None/ডিফল্ট দেয়।

English: Normal access raises KeyError, .get() returns None/default.

🔹 Q: Python 3.9+ এ দুইটা dict merge কিভাবে করব?

d3 = d1 | d2


🔹 Q: dict keys আর values কিভাবে লুপ করব?

for k,v in my_dict.items():
    print(k,v)


🔹 Q: list কি dictionary key হতে পারে? (Can list be key?)

বাংলা উত্তর: না, কারণ list mutable।

English: No, because keys must be immutable.

🔹 Q: dictionary কে values দিয়ে sort কিভাবে করব?

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))


🔹 Q: একই key দুইবার দিলে কী হবে? (Duplicate key?)

বাংলা উত্তর: শেষের ভ্যালু আগেরটাকে ওভাররাইট করবে।

English: The last value overrides the first.

d = {"a":1,"a":2}
print(d)  # {'a':2}
