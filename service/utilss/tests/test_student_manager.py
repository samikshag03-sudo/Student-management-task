"""Unit tests for StudentManager (pytest)."""
import tempfile
import os
from services.student_manager import StudentManager, StudentNotFoundError, DuplicateStudentError
from models.student import Student


def test_add_get_delete(tmp_path):
    path = tmp_path / "students.json"
    mgr = StudentManager(str(path))
    s = Student("s1", "Alice", 20, "A", "alice@example.com")
    mgr.add_student(s)
    got = mgr.get_student("s1")
    assert got.name == "Alice"
    mgr.delete_student("s1")
    try:
        mgr.get_student("s1")
        assert False, "Should have raised"
    except StudentNotFoundError:
        pass


def test_duplicate(tmp_path):
    path = tmp_path / "students.json"
    mgr = StudentManager(str(path))
    s = Student("s2", "Bob", 21, "B")
    mgr.add_student(s)
    try:
        mgr.add_student(s)
        assert False, "Should have raised DuplicateStudentError"
    except DuplicateStudentError:
        pass

