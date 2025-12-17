class Student:
    college = "ABC college"

    def __init__(self,name):
        self.name = name

s1 = Student("Kartik")
s2 = Student("Kunwar")

print(s1.college)
print(s2.college)
Student.college = "XYZ College"
print(s1.college)
print(s2.college)