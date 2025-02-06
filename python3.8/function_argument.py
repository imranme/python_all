def show_double(x):
    print(x*2)

show_double(2)
show_double(100)


# পাইথনে * এর অর্থ
# * এর আর্গুমেন্টে ভ্যালু Tuple হিসেবে প্যাকড থাকে। এর মানে * দিয়ে প্যারামিটার ডিক্লেয়ার করলে আমরা যেকোন সংখ্যক পজিশনাল আর্গুমেন্ট পাস করতে পারি। যেমন করলাম make_sum এর ক্ষেত্রে। শুরুতে make_sum মাত্র দুইটা আর্গুমেন্ট নিলেও পরবর্তীতে আমরা প্যারামিটারে * বসিয়ে দিলাম তখন সে অনেকগুলো আর্গুমেন্ট পাস করতে পারছে।

def make_sum(*args):
    sum = 0
    for num in args: # Here, args is like a Tuple which is (10, 20, 30, 40)
        sum += num
    return sum

print(make_sum(10, 20, 30, 40))

def add_numbers(x, y):
    total = x + y
    return total
       

print(add_numbers(4, 5))