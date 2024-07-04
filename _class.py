from typing import List
from human import Human
import csv

class Class(Human):
  def __init__(self, _grade, _letter, _students: List["Student"], _homeroom_teacher: "Teacher"):
    _grade: int
    _letter: str
    _students: List["Student"]
    _homeroom_teacher: "Teacher"

    def __getitem__(self):
        for el in self._students:
          print(sorted(el))
    def __list__(self):
       for el in self._students.lower():
        if el == str_student:
          return f"{self.__students.append(el)}"

    def __hash__(self):
        return hash((self.name, self.last_name, self.__id))

    def __lt__(self, other):
        return (self.last_name, self.name) < (other.last_name, other.name)

    def __repr__(self):
        return f" (Имя = '{self.name}', Фамилия = '{self.last_name}', id={self.__id})"

    def __str__(self):
        return f"{self.name} {self.last_name}"