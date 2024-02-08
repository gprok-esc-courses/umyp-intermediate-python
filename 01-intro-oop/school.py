

class School:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        s = Student(name)
        self.students.append(s)

    def print_students(self):
        for student in self.students:
            print(student)

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def __str__(self):
        return self.name

    def add_grade(self, grade):
        self.grades.append(grade)


school = School()
school.add_student('Jayden')
school.add_student('Tole')
school.print_students()

# a = Student('Jayden')
# b = Student('Tole')
# a.add_grade(89)
# a.add_grade(90)
#
# print(a)
# print(a.grades)
# print(b)
