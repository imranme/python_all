# ২. স্টুডেন্ট ও কোর্স

# একটি Student ক্লাস বানাও, যেখানে নাম, রোল নম্বর এবং কোন কোন কোর্সে ভর্তি হয়েছে সেই তথ্য থাকবে।
# এতে মেথড থাকবে:

# নতুন কোর্সে ভর্তি হওয়া (enroll in course)

# সব ভর্তি করা কোর্স দেখা (view courses)

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def view_couress(self):
        return self.courses
    
s1 = Student("tushar", 101)
s1.enroll("Python")
s1.enroll("OOP")
print("tushar courses:", s1.view_couress())
