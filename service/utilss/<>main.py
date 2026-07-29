"""CLI for Student Management System."""
import sys
from services.student_manager import StudentManager, StudentNotFoundError, DuplicateStudentError
from models.student import Student
from utils.validators import is_valid_email, assert_non_empty_str, assert_positive_int


def prompt_student_data() -> Student:
    sid = input("Student ID: ").strip()
    assert_non_empty_str(sid, "Student ID")
    name = input("Name: ").strip()
    assert_non_empty_str(name, "Name")
    age_raw = input("Age: ").strip()
    try:
        age = int(age_raw)
    except ValueError:
        raise ValueError("Age must be an integer.")
    assert_positive_int(age, "Age")
    grade = input("Grade: ").strip()
    assert_non_empty_str(grade, "Grade")
    email = input("Email (optional): ").strip()
    if not is_valid_email(email):
        raise ValueError("Invalid email format.")
    return Student(student_id=sid, name=name, age=age, grade=grade, email=email)


def print_student(s: Student) -> None:
    print(f"- ID: {s.student_id}, Name: {s.name}, Age: {s.age}, Grade: {s.grade}, Email: {s.email}")


def main():
    mgr = StudentManager()
    actions = {
        "1": "Add student",
        "2": "Update student",
        "3": "Delete student",
        "4": "View student",
        "5": "List all students",
        "6": "Search students",
        "0": "Exit",
    }

    while True:
        print("\nStudent Management - choose an action:")
        for k, v in actions.items():
            print(f"{k}. {v}")
        choice = input("> ").strip()
        try:
            if choice == "1":
                s = prompt_student_data()
                try:
                    mgr.add_student(s)
                    print("Student added.")
                except DuplicateStudentError as e:
                    print("Error:", e)
            elif choice == "2":
                sid = input("Student ID to update: ").strip()
                field = input("Field to update (name/age/grade/email): ").strip()
                value = input("New value: ").strip()
                if field == "age":
                    value = int(value)
                mgr.update_student(sid, **{field: value})
                print("Updated.")
            elif choice == "3":
                sid = input("Student ID to delete: ").strip()
                mgr.delete_student(sid)
                print("Deleted.")
            elif choice == "4":
                sid = input("Student ID: ").strip()
                s = mgr.get_student(sid)
                print_student(s)
            elif choice == "5":
                for s in mgr.list_students():
                    print_student(s)
            elif choice == "6":
                name = input("Name contains (leave empty to skip): ").strip() or None
                grade = input("Grade equals (leave empty to skip): ").strip() or None
                min_age = input("Min age (enter to skip): ").strip()
                min_age = int(min_age) if min_age else None
                max_age = input("Max age (enter to skip): ").strip()
                max_age = int(max_age) if max_age else None
                results = mgr.search(name=name, grade=grade, min_age=min_age, max_age=max_age)
                print(f"{len(results)} result(s):")
                for s in results:
                    print_student(s)
            elif choice == "0":
                print("Goodbye.")
                sys.exit(0)
            else:
                print("Unknown choice.")
        except (ValueError, StudentNotFoundError) as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()
