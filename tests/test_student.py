from src.student import Student

class TestStudent:
    def test_student_creation(self):
        # When
        student = Student("John", "Doe", 12345)

        # Then
        assert student.first_name == "John"
        assert student.last_name == "Doe"
        assert student.student_id == 12345

    def test_student_update(self):
        # Given
        student = Student("John", "Doe", 12345)

        # When
        student.update_info("Johnny", "Doe")

        # Then
        assert student.first_name == "Johnny"
        assert student.last_name == "Doe"

    def test_student_equality(self):
        # Given
        student1 = Student("John", "Doe", 12345)
        student2 = Student("Jane", "Smith", 12345)

        # Then
        assert student1 == student2

    def test_student_inequality(self):
        # Given
        student1 = Student("John", "Doe", 12345)
        student2 = Student("Jane", "Smith", 54321)

        # Then
        assert student1 != student2
