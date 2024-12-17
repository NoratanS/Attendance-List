from src.student import Student
from src.group import Group

class TestAttendance:
    def test_mark_attendance(self):
        # Given
        test_group = Group("Test Group")
        student1 = Student("John", "Doe", 12345)
        student2 = Student("Jane", "Smith", 54321)
        test_group.add_student(student1)
        test_group.add_student(student2)

        # When
        test_group.mark_student_attendance(student1, True)
        test_group.mark_student_attendance(student2, False)

        # Then
        assert test_group.attendance_list[student1] == 1
        assert test_group.attendance_list[student2] == 0

    def test_edit_attendance(self):
        # Given
        test_group = Group("Test Group")
        student1 = Student("John", "Doe", 12345)
        student2 = Student("Jane", "Smith", 54321)
        test_group.add_student(student1)
        test_group.add_student(student2)
        test_group.mark_student_attendance(student1, True)
        test_group.mark_student_attendance(student2, False)

        # When
        test_group.edit_attendance(student1, False)
        test_group.edit_attendance(student2, True)

        # Then
        assert test_group.attendance_list[student1] == 0
        assert test_group.attendance_list[student2] == 1
