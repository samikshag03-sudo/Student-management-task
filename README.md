# Student-management-task
# Student Management System (Python)

A simple modular student management system demonstrating:
- CRUD operations for students
- Object-Oriented Programming
- File-based persistence (JSON file)
- Search & filter
- Exception handling
- Unit tests with pytest

Getting started:
1. Create a virtualenv: `python -m venv venv && source venv/bin/activate`
2. Install deps: `pip install -r requirements.txt`
3. Run: `python main.py`
4. Run tests: `pytest -q`

Project structure:
- models/student.py - Student dataclass
- storage/file_handler.py - JSON persistence
- services/student_manager.py - CRUD + search logic
- utils/validators.py - small validation helpers
- main.py - CLI
- data/students.json - runtime data file (auto-created)
- tests/ - unit tests

How to contribute:
- Open issues and pull requests on the repository.
- Add features (import/export CSV, GUI, REST API).

