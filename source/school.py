
class TooManyStudents(Exception):
    pass

class Classroom:
    
    def __init__(self, teacher, students, course_title):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title
    
    def add_students(self, student):
        if len(self.students) < 10:
            self.students.append(student)
        else:
            raise TooManyStudents
    
    def remove_students(self, students_list):
        for student in list(self.students):
            if student.name in students_list:
                self.students.remove(student)
        
    def change_teacher(self, new_teacher):
        self.teacher = new_teacher


class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    pass

class Student(Person):
    pass

