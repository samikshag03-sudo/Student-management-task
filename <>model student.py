"""Student model with serialization helpers."""
from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class Student:
    student_id: str
    name: str
    age: int
    grade: str
    email: str = ""

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def from_dict(d: Dict) -> "Student":
        return Student(
            student_id=d["student_id"],
            name=d["name"],
            age=int(d["age"]),
            grade=d["grade"],
            email=d.get("email", ""),
        )

Storage/file_handler.py

"""Simple JSON file handler for reading/writing student records."""
import json
from typing import List, Dict
from pathlib import Path


class FileHandler:
    def __init__(self, filepath: str):
        self.path = Path(filepath)
        if not self.path.exists():
            self._write_data([])

    def _read_raw(self) -> List[Dict]:
        try:
            with self.path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _write_data(self, data: List[Dict]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def read_all(self) -> List[Dict]:
        return self._read_raw()

    def write_all(self, data: List[Dict]) -> None:
        self._write_data(data)

