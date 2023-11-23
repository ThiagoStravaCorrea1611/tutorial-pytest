
import pytest
from source.school import Student, Teacher, TooManyStudents


def test_add_students(empty_classroom):
    # Test adding students to an empty classroom
    empty_classroom.add_students(Student("Harry"))
    assert len(empty_classroom.students) == 1
    assert empty_classroom.students[0].name == "Harry"

    # Test adding too many students
    with pytest.raises(TooManyStudents):
        for _ in range(10):
            empty_classroom.add_students(Student("RandomStudent"))

    assert len(empty_classroom.students) == 10


def test_remove_students(full_classroom):
    # Test removing existing students
    full_classroom.remove_students(["Harry", "Hermione", "Ron"])
    assert "Harry" not in [x.name for x in full_classroom.students]
    assert "Hermione" not in [x.name for x in full_classroom.students]
    assert "Ron" not in [x.name for x in full_classroom.students]
    assert len(full_classroom.students) == 4

    # Test removing non-existing students
    full_classroom.remove_students(["Neville", "Luna", "Draco"])
    assert len(full_classroom.students) == 4


def test_change_teacher(full_classroom):
    # Test changing the teacher
    assert full_classroom.teacher.name == "Professor McGonagall"
    new_teacher = Teacher("Professor Flitwick")
    full_classroom.change_teacher(new_teacher)
    assert full_classroom.teacher.name == "Professor Flitwick"
