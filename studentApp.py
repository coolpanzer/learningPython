# from File import Class name
from Student import Student

# Make an instance of the Student class
student1 = Student("Ranz", "Business", 3.1, False)
student2 = Student("Ryah", "Architecture", 3.6, False)
student1 = Student("Rev", "Engineering", 3.1, False)

print(student1.gpa)
print(student2.major)
print(student2.on_honor_roll())