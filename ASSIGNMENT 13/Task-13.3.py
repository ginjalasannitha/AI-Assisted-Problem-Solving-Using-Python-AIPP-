# ...existing code...
from dataclasses import dataclass, field
from typing import Iterable, List


@dataclass(slots=True)
class Student:
    """Represents a student with a name, age, and a collection of marks."""

    name: str
    age: int
    marks: List[int] = field(default_factory=list)

    def __post_init__(self) -> None:  # <-- renamed to run automatically
        """Validate and normalize incoming data."""
        self.name = self.name.strip()
        if self.age <= 0:
            raise ValueError("Age must be positive")
        self.marks = [self._validate_mark(mark) for mark in self.marks]

    @staticmethod
    def _validate_mark(mark: int) -> int:
        if not 0 <= mark <= 100:
            raise ValueError("Marks must be between 0 and 100")
        return int(mark)

    def add_marks(self, new_marks: Iterable[int]) -> None:
        """Add additional marks after validation."""
        for mark in new_marks:
            self.marks.append(self._validate_mark(mark))

    def details(self) -> str:
        """Return a formatted string of the student's details."""
        return f"Name: {self.name}, Age: {self.age}"

    def total(self) -> int:
        """Return the sum of the student's marks."""
        return sum(self.marks)

    def average(self) -> float:
        """Return the average of the student's marks."""
        return self.total() / len(self.marks) if self.marks else 0.0


if __name__ == "__main__":
    # small demo so running the script produces output
    s = Student("  Alice  ", 20, [90, 80, 95])
    print(s.details())
    print("Marks:", s.marks)
    print("Total:", s.total())
    print("Average:", s.average())
# ...existing code...