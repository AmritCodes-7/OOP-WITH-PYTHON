class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        # adding student if the list is not full
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        sum = 0
        for student in self.students:
            sum += student.get_grade()  # finding the sum of the grades
        return sum / len(self.students)


s1 = Student("Amrit", 20, 90)
s2 = Student("Auraj", 21, 95)
s3 = Student("Raj", 21, 80)

# the name of the course wil be BEI and the maximum number of students it can hold will be 2
course = Course("BEI", 2)
course.add_student(s1)
course.add_student(s2)
# course.add_student(s3) # this will not be added to the students list

# print(course.students[0].name) # returns the name of the student in first index
print(course.add_student(s3)) # prints false as it cannot hold the data of three students 
print(course.get_average_grade())
