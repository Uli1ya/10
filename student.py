from human import Human
class Student(Human):
  def __init__(self):
    super().__init__(name, last_name)
    _class: Class
  def set_class(self, new_class):
      self._class = new_class


  def get_class(self):
    return self._class