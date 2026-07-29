"""Business logic: StudentManager providing CRUD, search, filter operations."""
from typing import List, Dict, Optional
from models.student import Student
from storage.file_handler import FileHandler


class StudentNotFoundError(Exception):
    pass


class DuplicateStudentError(Exception):
    pass


class StudentManager:
    def __init__(self, storage_path: str = "data/students.json"):
        self.store = FileHandler(storage_path)

    def _load_students(self) -> List[Student]:
        raw = self.store.read_all()
        return [Student.from_dict(d) for d in raw]

    def _save_students(self, students: List[Student]) -> None:
        self.store.write_all([s.to_dict() for s in students])

    def add_student(self, student: Student) -> None:
        students = self._load_students()
        if any(s.student_id == student.student_id for s in students):
            raise DuplicateStudentError(f"Student with id {student.student_id} already exists.")
        students.append(student)
        self._save_students(students)

    def update_student(self, student_id: str, **fields) -> None:
        students = self._load_students()
        for i, s in enumerate(students):
            if s.student_id == student_id:
                updated = {**s.to_dict(), **fields}
                students[i] = Student.from_dict(updated)
                self._save_students(students)
                return
        raise StudentNotFoundError(f"Student {student_id} not found.")

    def delete_student(self, student_id: str) -> None:
        students = self._load_students()
        new = [s for s in students if s.student_id != student_id]
        if len(new) == len(students):
            raise StudentNotFoundError(f"Student {student_id} not found.")
        self._save_students(new)

    def get_student(self, student_id: str) -> Student:
        students = self._load_students()
        for s in students:
            if s.student_id == student_id:
                return s
        raise StudentNotFoundError(f"Student {student_id} not found.")

    def list_students(self) -> List[Student]:
        return self._load_students()

    def search(self, name: Optional[str] = None, grade: Optional[str] = None,
               min_age: Optional[int] = None, max_age: Optional[int] = None) -> List[Student]:
        results = self._load_students()
        if name:
            q = name.lower()
            results = [s for s in results if q in s.name.lower()]
        if grade:
            results = [s for s in results if s.grade.lower() == grade.lower()]
        if min_age is not None:
            results = [s for s in results if s.age >= min_age]
        if max_age is not None:
            results = [s for s in results if s.age <= max_age]
        return results
