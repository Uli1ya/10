from human import Human
from subject import Subject
from typing import List
from _class import Class


class Teacher(Human):
    def __init__(self, _subjects: List[Subject], _homeroom_class: Class | None):
        super().__init__(name, last_name)
        self._homeroom_class = _homeroom_class
        self._subjects =_subjects

    def set_class(self, _homeroom_class):
        self._homeroom_class = _homeroom_class

    def get_class(self):
        return f"{self._homeroom_class}"