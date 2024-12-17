import pytest
from src.student import Student
from src.group import Group

class TestImport:
    def test_import(self):
        # Given
        test_group2 = Group("Test Group")

        # When
        test_group2.import_data("tests/test_group_good.txt")

        expected_content = {
            Student("John", "Doe", 12345): 0,
            Student("Jane", "Smith", 54321): 0
        }

        # Then
        assert test_group2.attendance_list == expected_content

    def test_import_empty(self):
        # Given
        test_group = Group("Test Group")

        # When
        test_group.import_data("tests/test_group_empty.txt")

        expected_content = {}

        # Then
        assert test_group.attendance_list == expected_content

    def test_import_wrong(self):
        # Given
        test_group = Group("Test Group")

        # When and Then
        with pytest.raises(ValueError):
            test_group.import_data("tests/test_group_wrong.txt")
