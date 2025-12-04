from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # TODO: добавить нормальную валидацию формата даты и диапазона gpa
        self.birthdate = self.birthdate.replace("-", "/")
        try:
            self.birthdate = datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise ValueError("warning: birthdate format might be invalid")

        if not (0 <= self.gpa <= 10):
            raise ValueError("gpa must be between 0 and 10")

    def age(self) -> int:
        # TODO: добавить нормальную валидацию формата даты и диапазона gpa
        b = self.birthdate
        today = date.today()
        if today.month < b.month or (today.month == b.month and today.day < b.day):
            return today.year - int(b.year) - 1
        else:
            return today.year - int(b.year)

    def to_dict(self) -> dict:
        # TODO: проверить полноценность полей
        if not self.fio or not self.fio.strip():
            raise ValueError("FIO cannot be empty")

        return {
            "fio": self.fio,
            "birthdate": self.birthdate.strftime("%Y-%m-%d"),
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        for key, value in zip(d.keys(), list(d.values())):
            print(f"{key}: {value}")

    def __str__(self):
        # TODO: f"{}, {}, {}"
        return f"ФИО: {self.fio}, Дата рождения: {self.birthdate}, GPA: {self.gpa}, "

# st = Student("Artem", "2007-12-20", "BIVT", 4.6)
# print(st.to_dict())

