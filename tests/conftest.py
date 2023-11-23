import pytest
import source.shapes as shapes
from source.school import Classroom, Teacher, Student, TooManyStudents


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)

@pytest.fixture
def empty_classroom():
    return Classroom(teacher=Teacher("Professor Snape"), students=[], course_title="Potions")


@pytest.fixture
def full_classroom():
    students = [Student("Harry"),
                Student("Hermione"),
                Student("Ron"),
                Student("Ginny"),
                Student("Fred"),
                Student("George"),
                Student("Cho")]
    return Classroom(
        teacher=Teacher("Professor McGonagall"),
        students=students,
        course_title="Transfiguration")
